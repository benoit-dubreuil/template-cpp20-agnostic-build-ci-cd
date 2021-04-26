__all__ = ['EnvMSVC']

import contextlib
import os
import subprocess
from typing import Final, MutableMapping, Optional

from .msvc import *


class EnvMSVC(contextlib.AbstractContextManager):
    compiler: Final[MSVCCompilerInstance]
    vcvars: Optional[dict[str, list[str]]]

    def __init__(self, compiler: MSVCCompilerInstance) -> None:
        super().__init__()
        self.compiler = compiler
        self.vcvars = None

    def __enter__(self):
        self.__setup_env()
        self.compiler.cache_vcvars_as_compiler_env(vcvars=self.vcvars)

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

        for vcvar_key, vcvar_value in self.vcvars.items():
            formatted_vcvar_value = os.pathsep.join(vcvar_value)

            if vcvar_key in local_env and len(local_env[vcvar_key]) > 0:
                matching_local_env_var_value = local_env[vcvar_key]

                if matching_local_env_var_value[-1] != os.pathsep:
                    matching_local_env_var_value += os.pathsep

                local_env[vcvar_key] = matching_local_env_var_value + formatted_vcvar_value
            else:
                local_env[vcvar_key] = formatted_vcvar_value

    def __remove_vcvars_from_local_env(self):
        local_env = os.environ

        for vcvar_key, vcvar_value in self.vcvars.items():
            if vcvar_key in local_env:
                formatted_vcvar_value = os.pathsep.join(vcvar_value)

                matching_local_env_var_value = local_env[vcvar_key]

                # Replace instead of search -> KISS
                new_matching_local_env_var_value = matching_local_env_var_value.replace(formatted_vcvar_value, str())
                new_matching_local_env_var_value = new_matching_local_env_var_value.strip(os.pathsep + ' ')

                if len(new_matching_local_env_var_value) <= 0:
                    del local_env[vcvar_key]
                else:
                    local_env[vcvar_key] = new_matching_local_env_var_value

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
                split_values: list[str] = env_var_value.strip().split(sep=os.pathsep)
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
