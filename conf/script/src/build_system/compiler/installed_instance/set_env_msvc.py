import contextlib
import os
import subprocess
from typing import Final, MutableMapping, Optional

_ENV_VAR_MULTI_VALUES_SEP: Final[str] = ';'


class EnvMSVC(contextlib.AbstractContextManager):
    import build_system.compiler.installed_instance.msvc

    compiler: build_system.compiler.installed_instance.msvc.MSVCCompilerInstance
    vcvars: Optional[dict[str, list[str]]]

    def __init__(self, compiler: build_system.compiler.installed_instance.msvc.MSVCCompilerInstance) -> None:
        super().__init__()
        self.compiler = compiler
        self.vcvars = None

    def __enter__(self):
        self.__setup_env()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.__teardown_env()
        return False

    def get_env(self) -> dict[str, list[str]]:
        assert self.vcvars is not None
        return self.vcvars

    def __setup_env(self) -> None:
        local_env: dict[str, list[str]] = self.__interpret_local_en_vars()
        all_vcvars = self.__fetch_all_vcvars()
        vcvars = self.__except_local_env_from_vcvars(local_env=local_env, all_vcvars=all_vcvars)

        self.vcvars = vcvars

        self.__append_vcvars_to_local_env()

    def __teardown_env(self) -> None:
        self.__remove_vcvars_from_local_env()
        self.vcvars = None

    def __append_vcvars_to_local_env(self):
        local_env = os.environ

        for vcvars_var_key, vcvars_var_value in self.vcvars.items():
            formatted_vcvars_var_value = _ENV_VAR_MULTI_VALUES_SEP.join(vcvars_var_value)

            if vcvars_var_key in local_env and len(local_env[vcvars_var_key]) > 0:
                matching_local_env_var_value = local_env[vcvars_var_key]

                if matching_local_env_var_value[-1] != _ENV_VAR_MULTI_VALUES_SEP:
                    matching_local_env_var_value += _ENV_VAR_MULTI_VALUES_SEP

                local_env[vcvars_var_key] = matching_local_env_var_value + formatted_vcvars_var_value
            else:
                local_env[vcvars_var_key] = formatted_vcvars_var_value

    def __remove_vcvars_from_local_env(self):
        local_env = os.environ

        for vcvars_var_key, vcvars_var_value in self.vcvars.items():
            if vcvars_var_key in local_env:
                formatted_vcvars_var_value = _ENV_VAR_MULTI_VALUES_SEP.join(vcvars_var_value)

                matching_local_env_var_value = local_env[vcvars_var_key]

                # Replace instead of search -> KISS
                new_matching_local_env_var_value = matching_local_env_var_value.replace(formatted_vcvars_var_value, str())
                new_matching_local_env_var_value = new_matching_local_env_var_value.strip(_ENV_VAR_MULTI_VALUES_SEP + ' ')

                if len(new_matching_local_env_var_value) <= 0:
                    del local_env[vcvars_var_key]
                else:
                    local_env[vcvars_var_key] = new_matching_local_env_var_value

    @staticmethod
    def __except_local_env_from_vcvars(local_env: dict[str, list[str]], all_vcvars: dict[str, list[str]]) -> dict[str, list[str]]:
        vcvars_except_local_env: dict[str, list[str]] = {}

        for vcvar_env_var_key, vcvar_env_var_value in all_vcvars.items():
            vcvar_env_var_value_except_local_env_var: list[str]

            if vcvar_env_var_key in local_env:
                vcvar_env_var_value_except_local_env_var = []
                local_env_var_value: list[str] = local_env[vcvar_env_var_key]

                for vcvar_env_var_value_element in vcvar_env_var_value:
                    if vcvar_env_var_value_element not in local_env_var_value:
                        vcvar_env_var_value_except_local_env_var.append(vcvar_env_var_value_element)
            else:
                vcvar_env_var_value_except_local_env_var = vcvar_env_var_value.copy()

            if len(vcvar_env_var_value_except_local_env_var) > 0:
                vcvars_except_local_env[vcvar_env_var_key] = vcvar_env_var_value_except_local_env_var

        return vcvars_except_local_env

    @staticmethod
    def __interpret_local_en_vars() -> dict[str, list[str]]:
        local_env: MutableMapping[str, str] = os.environ
        interpreted_local_env: dict[str, list[str]] = {}

        for env_var_key, env_var_value in local_env.items():
            if (env_var_value is not None) and (len(env_var_value) > 0):
                split_values: list[str] = env_var_value.strip().split(sep=_ENV_VAR_MULTI_VALUES_SEP)
                interpreted_local_env[env_var_key.upper()] = split_values

        return interpreted_local_env

    def __fetch_all_vcvars(self) -> dict[str, list[str]]:
        shell_env: str = self.__shell_get_vcvars()
        vcvars: dict[str, list[str]] = self.__interpret_shell_vcvars(shell_env=shell_env)

        assert len(vcvars) > 0
        return vcvars

    @staticmethod
    def __interpret_shell_vcvars(shell_env: str) -> dict[str, list[str]]:
        vcvars: dict[str, list[str]] = {}

        for env_var in shell_env.splitlines():
            env_var_key, env_var_grouped_values = env_var.split(sep='=', maxsplit=1)
            env_var_split_values = env_var_grouped_values.split(sep=';')

            vcvars[env_var_key.upper()] = env_var_split_values

        return vcvars

    def __shell_get_vcvars(self) -> str:
        timeout_in_seconds: Final[float] = 20
        arg_sep: Final[str] = ' '

        shell_interpreter: Final[str] = r'cmd'
        shell_interpreter_option_on_end: Final[str] = r'/c'
        shell_interpreter_redirect_to_null: Final[str] = arg_sep.join([r'>', os.devnull, r' 2>&1'])
        shell_logical_and: Final[str] = r'&&'

        cmd_vcvars_batch_file: Final[str] = '"' + str(self.compiler.vcvars_arch_batch_file) + '"'
        cmd_get_env: Final[str] = r'set'

        formed_cmd = arg_sep.join([shell_interpreter,
                                   shell_interpreter_option_on_end,
                                   cmd_vcvars_batch_file,
                                   shell_interpreter_redirect_to_null,
                                   shell_logical_and,
                                   cmd_get_env])

        return subprocess.check_output(formed_cmd, text=True, stderr=subprocess.DEVNULL, timeout=timeout_in_seconds)
