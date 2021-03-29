import os
import subprocess
from pathlib import Path
from typing import Final, final

import build_system.compiler
import build_system.compiler.family
import build_system.compiler.installed_instance.compiler_instance
import utils.error.cls_def
import utils.error.try_external_errors

_ENV_VAR_MULTI_VALUES_SEP: Final[str] = ';'


@final
class MSVCCompilerInstance(build_system.compiler.installed_instance.CompilerInstance):
    vcvars_arch_batch_file: Path
    vcvars_en_vars: {str: list[str]}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        object.__setattr__(self, 'vcvars_arch_batch_file', self.__find_vcvars_batch_file())
        object.__setattr__(self, 'vcvars_en_vars', [])

    @classmethod
    def _find_installation_dir_by_compiler_family(cls, compiler_family: build_system.compiler.family.CompilerFamily) -> Path:
        import build_system.cmd.compiler.host.get_info.location.msvc

        cls._assert_compiler_family(compiler_family=compiler_family)

        compiler_installation_dir = build_system.cmd.compiler.host.get_info.location.msvc.find_location()
        return compiler_installation_dir

    @staticmethod
    def get_supported_compiler_families() -> list[build_system.compiler.family.CompilerFamily]:
        return [build_system.compiler.family.CompilerFamily.MSVC]

    @staticmethod
    def get_vcvars_dir_relative_to_installation_dir() -> Path:
        return Path('VC/Auxiliary/Build')

    @staticmethod
    def get_vcvars_prefix() -> str:
        return 'vcvars'

    @staticmethod
    def get_vcvars_extension() -> str:
        return '.bat'

    @staticmethod
    def requires_env_vars_setup() -> bool:
        return True

    def setup_env_vars(self) -> None:
        vcvars_en_vars = self.__fetch_all_vcvars_env_vars()
        object.__setattr__(self, 'vcvars_en_vars', vcvars_en_vars)

        # TODO
        ...

    def teardown_env_vars(self) -> None:
        # TODO
        ...

    def __get_vcvars_dir(self) -> Path:
        vcvars_dir: Path = self.installation_dir / self.get_vcvars_dir_relative_to_installation_dir()

        utils.error.try_external_errors.try_manage_strict_path_resolving(path_to_resolve=vcvars_dir,
                                                                         external_errors_to_manage={(Exception,): utils.error.cls_def.MSVCCompilerVcvarsDirNotFoundError})

        return vcvars_dir

    def __compute_vcvars_arch_batch_filename(self) -> str:
        return self.get_vcvars_prefix() + str(self.arch.value) + self.get_vcvars_extension()

    def __find_vcvars_batch_file(self) -> Path:
        vcvars_dir: Path = self.__get_vcvars_dir()
        vcvars_filename: str = self.__compute_vcvars_arch_batch_filename()
        vcvars_arch_batch_file = vcvars_dir / vcvars_filename
        vcvars_arch_batch_file = vcvars_arch_batch_file.absolute()

        utils.error.try_external_errors.try_manage_strict_path_resolving(path_to_resolve=vcvars_arch_batch_file,
                                                                         external_errors_to_manage={(Exception,): utils.error.cls_def.MSVCCompilerVcvarsBatchFileNotFoundError})

        return vcvars_arch_batch_file

    def __append_vcvars_to_local_env_vars(self):
        local_env_vars = os.environ

        for vcvars_env_var_key, vcvars_env_var_value in self.vcvars_en_vars.items():
            if vcvars_env_var_key in local_env_vars and len(local_env_vars[vcvars_env_var_key]) > 0:
                matching_local_env_var_value = local_env_vars[vcvars_env_var_key]

                if matching_local_env_var_value[-1] != _ENV_VAR_MULTI_VALUES_SEP:
                    matching_local_env_var_value += _ENV_VAR_MULTI_VALUES_SEP

                # Append in order to easily remove the env vars later
                local_env_vars[vcvars_env_var_key] = matching_local_env_var_value + vcvars_env_var_value
            else:
                local_env_vars[vcvars_env_var_key] = vcvars_env_var_value

    def __remove_vcvars_from_local_env_vars(self):
        local_env_vars = os.environ

        for vcvars_env_var_key, vcvars_env_var_value in self.vcvars_en_vars.items():
            if vcvars_env_var_key in local_env_vars:
                matching_local_env_var_value = local_env_vars[vcvars_env_var_key]

                matching_local_env_var_value = matching_local_env_var_value.replace(vcvars_env_var_value, str())
                matching_local_env_var_value = matching_local_env_var_value.strip(_ENV_VAR_MULTI_VALUES_SEP + ' ')

                if len(matching_local_env_var_value) <= 0:
                    del local_env_vars[vcvars_env_var_key]
                else:
                    local_env_vars[vcvars_env_var_key] = matching_local_env_var_value

    def __fetch_all_vcvars_env_vars(self) -> {str: list[str]}:
        shell_env_vars: str = self.__shell_get_vcvars_env_vars()
        vcvars_en_vars: {str: list[str]} = self.__interpret_shell_vcvars_en_vars(shell_env_vars=shell_env_vars)

        assert len(vcvars_en_vars) > 0
        return vcvars_en_vars

    @staticmethod
    def __interpret_shell_vcvars_en_vars(shell_env_vars: str) -> {str: list[str]}:
        vcvars_en_vars: {str: list[str]} = {}

        for env_var in shell_env_vars.splitlines():
            env_var_key, env_var_grouped_values = env_var.split(sep='=', maxsplit=1)
            env_var_split_values = env_var_grouped_values.split(sep=';')

            vcvars_en_vars[env_var_key] = env_var_split_values

        return vcvars_en_vars

    def __shell_get_vcvars_env_vars(self) -> str:
        timeout_in_seconds: Final[float] = 20
        arg_sep: Final[str] = ' '

        shell_interpreter: Final[str] = r'cmd'
        shell_interpreter_option_on_end: Final[str] = r'/c'
        shell_interpreter_redirect_to_null: Final[str] = arg_sep.join([r'>', os.devnull, r' 2>&1'])
        shell_logical_and: Final[str] = r'&&'

        cmd_vcvars_batch_file: Final[str] = '"' + str(self.vcvars_arch_batch_file) + '"'
        cmd_get_env_vars: Final[str] = r'set'

        formed_cmd = arg_sep.join([shell_interpreter,
                                   shell_interpreter_option_on_end,
                                   cmd_vcvars_batch_file,
                                   shell_interpreter_redirect_to_null,
                                   shell_logical_and,
                                   cmd_get_env_vars])

        return subprocess.check_output(formed_cmd, text=True, stderr=subprocess.DEVNULL, timeout=timeout_in_seconds)
