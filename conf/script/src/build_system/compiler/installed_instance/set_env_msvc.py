import contextlib
import os
import subprocess
from typing import Final, MutableMapping


_ENV_VAR_MULTI_VALUES_SEP: Final[str] = ';'


class EnvMSVC(contextlib.AbstractContextManager):
    import build_system.compiler.installed_instance.msvc

    compiler: build_system.compiler.installed_instance.msvc.MSVCCompilerInstance

    def __init__(self, compiler: build_system.compiler.installed_instance.msvc.MSVCCompilerInstance) -> None:
        super().__init__()
        self.compiler = compiler

    def __enter__(self):
        self.__setup_env_vars()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.__teardown_env_vars()
        return False

    def __setup_env_vars(self) -> None:
        local_env_vars: dict[str, list[str]] = self.__interpret_local_en_vars()
        all_vcvars_en_vars = self.__fetch_all_vcvars_env_vars()
        vcvars_en_vars = self.__except_local_env_vars_from_vcvars_env_vars(local_env_vars=local_env_vars, all_vcvars_env_vars=all_vcvars_en_vars)

        object.__setattr__(self, 'vcvars_en_vars', vcvars_en_vars)

        self.__append_vcvars_to_local_env_vars()

    def __teardown_env_vars(self) -> None:
        self.__remove_vcvars_from_local_env_vars()
        object.__setattr__(self, 'vcvars_en_vars', None)

    def __append_vcvars_to_local_env_vars(self):
        local_env_vars = os.environ

        for vcvars_env_var_key, vcvars_env_var_value in self.compiler.vcvars_en_vars.items():
            formatted_vcvars_env_var_value = _ENV_VAR_MULTI_VALUES_SEP.join(vcvars_env_var_value)

            if vcvars_env_var_key in local_env_vars and len(local_env_vars[vcvars_env_var_key]) > 0:
                matching_local_env_var_value = local_env_vars[vcvars_env_var_key]

                if matching_local_env_var_value[-1] != _ENV_VAR_MULTI_VALUES_SEP:
                    matching_local_env_var_value += _ENV_VAR_MULTI_VALUES_SEP

                local_env_vars[vcvars_env_var_key] = matching_local_env_var_value + formatted_vcvars_env_var_value
            else:
                local_env_vars[vcvars_env_var_key] = formatted_vcvars_env_var_value

    def __remove_vcvars_from_local_env_vars(self):
        local_env_vars = os.environ

        for vcvars_env_var_key, vcvars_env_var_value in self.compiler.vcvars_en_vars.items():
            if vcvars_env_var_key in local_env_vars:
                formatted_vcvars_env_var_value = _ENV_VAR_MULTI_VALUES_SEP.join(vcvars_env_var_value)

                matching_local_env_var_value = local_env_vars[vcvars_env_var_key]

                # Replace instead of search -> KISS
                new_matching_local_env_var_value = matching_local_env_var_value.replace(formatted_vcvars_env_var_value, str())
                new_matching_local_env_var_value = new_matching_local_env_var_value.strip(_ENV_VAR_MULTI_VALUES_SEP + ' ')

                if len(new_matching_local_env_var_value) <= 0:
                    del local_env_vars[vcvars_env_var_key]
                else:
                    local_env_vars[vcvars_env_var_key] = new_matching_local_env_var_value

    @staticmethod
    def __except_local_env_vars_from_vcvars_env_vars(local_env_vars: dict[str, list[str]], all_vcvars_env_vars: dict[str, list[str]]) -> dict[str, list[str]]:
        vcvars_env_vars_except_local_env_vars: dict[str, list[str]] = {}

        for vcvar_env_var_key, vcvar_env_var_value in all_vcvars_env_vars.items():
            vcvar_env_var_value_except_local_env_var: list[str]

            if vcvar_env_var_key in local_env_vars:
                vcvar_env_var_value_except_local_env_var = []
                local_env_var_value: list[str] = local_env_vars[vcvar_env_var_key]

                for vcvar_env_var_value_element in vcvar_env_var_value:
                    if vcvar_env_var_value_element not in local_env_var_value:
                        vcvar_env_var_value_except_local_env_var.append(vcvar_env_var_value_element)
            else:
                vcvar_env_var_value_except_local_env_var = vcvar_env_var_value.copy()

            if len(vcvar_env_var_value_except_local_env_var) > 0:
                vcvars_env_vars_except_local_env_vars[vcvar_env_var_key] = vcvar_env_var_value_except_local_env_var

        return vcvars_env_vars_except_local_env_vars

    @staticmethod
    def __interpret_local_en_vars() -> dict[str, list[str]]:
        local_env_vars: MutableMapping[str, str] = os.environ
        interpreted_local_env_vars: dict[str, list[str]] = {}

        for env_var_key, env_var_value in local_env_vars.items():
            if (env_var_value is not None) and (len(env_var_value) > 0):
                split_values: list[str] = env_var_value.strip().split(sep=_ENV_VAR_MULTI_VALUES_SEP)
                interpreted_local_env_vars[env_var_key.upper()] = split_values

        return interpreted_local_env_vars

    def __fetch_all_vcvars_env_vars(self) -> dict[str, list[str]]:
        shell_env_vars: str = self.__shell_get_vcvars_env_vars()
        vcvars_en_vars: dict[str, list[str]] = self.__interpret_shell_vcvars_en_vars(shell_env_vars=shell_env_vars)

        assert len(vcvars_en_vars) > 0
        return vcvars_en_vars

    @staticmethod
    def __interpret_shell_vcvars_en_vars(shell_env_vars: str) -> dict[str, list[str]]:
        vcvars_en_vars: dict[str, list[str]] = {}

        for env_var in shell_env_vars.splitlines():
            env_var_key, env_var_grouped_values = env_var.split(sep='=', maxsplit=1)
            env_var_split_values = env_var_grouped_values.split(sep=';')

            vcvars_en_vars[env_var_key.upper()] = env_var_split_values

        return vcvars_en_vars

    def __shell_get_vcvars_env_vars(self) -> str:
        timeout_in_seconds: Final[float] = 20
        arg_sep: Final[str] = ' '

        shell_interpreter: Final[str] = r'cmd'
        shell_interpreter_option_on_end: Final[str] = r'/c'
        shell_interpreter_redirect_to_null: Final[str] = arg_sep.join([r'>', os.devnull, r' 2>&1'])
        shell_logical_and: Final[str] = r'&&'

        cmd_vcvars_batch_file: Final[str] = '"' + str(self.compiler.vcvars_arch_batch_file) + '"'
        cmd_get_env_vars: Final[str] = r'set'

        formed_cmd = arg_sep.join([shell_interpreter,
                                   shell_interpreter_option_on_end,
                                   cmd_vcvars_batch_file,
                                   shell_interpreter_redirect_to_null,
                                   shell_logical_and,
                                   cmd_get_env_vars])

        return subprocess.check_output(formed_cmd, text=True, stderr=subprocess.DEVNULL, timeout=timeout_in_seconds)
