import contextlib
from dataclasses import dataclass
from pathlib import Path
from typing import final, Optional

import build_system.compiler.build_option.sanitizer
import build_system.compiler.family
import build_system.compiler.installed_instance.compiler_instance
import utils.error.cls_def
import utils.error.try_external_errors


@final
@dataclass(order=True, frozen=True)
class MSVCCompilerInstance(build_system.compiler.installed_instance.CompilerInstance):
    vcvars_arch_batch_file: Path
    cached_compiler_env: Optional[dict[str, list[str]]]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        object.__setattr__(self, 'vcvars_arch_batch_file', self.__find_vcvars_batch_file())

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
    def get_supported_sanitizers() -> list[build_system.compiler.build_option.sanitizer.CompilerSanitizer]:
        return [build_system.compiler.build_option.sanitizer.CompilerSanitizer.NONE,
                build_system.compiler.build_option.sanitizer.CompilerSanitizer.ADDRESS]

    @staticmethod
    def get_vcvars_dir_relative_to_installation_dir() -> Path:
        return Path('VC/Auxiliary/Build')

    @staticmethod
    def get_vcvars_prefix() -> str:
        return 'vcvars'

    @staticmethod
    def get_vcvars_extension() -> str:
        return '.bat'

    def create_env_context_manager(self) -> contextlib.AbstractContextManager:
        import build_system.compiler.installed_instance.set_env_msvc
        return build_system.compiler.installed_instance.set_env_msvc.EnvMSVC(compiler=self)

    @staticmethod
    def has_export_shell_env_script() -> bool:
        return True

    def get_export_shell_env_script(self) -> Path:
        return self.vcvars_arch_batch_file

    def get_export_shell_env_script_extension(self) -> str:
        return self.get_vcvars_extension()

    @staticmethod
    def get_c_compiler_name() -> str:
        return 'cl'

    @staticmethod
    def get_cpp_compiler_name() -> str:
        return 'cl'

    def _cache_vcvars_as_compiler_env(self, vcvars: dict[str, list[str]]) -> None:
        object.__setattr__(self, 'cached_compiler_env', vcvars)

    def __find_vcvars_batch_file(self) -> Path:
        vcvars_dir: Path = self.__get_vcvars_dir()
        vcvars_filename: str = self.__compute_vcvars_arch_batch_filename()
        vcvars_arch_batch_file = vcvars_dir / vcvars_filename
        vcvars_arch_batch_file = vcvars_arch_batch_file.absolute()

        utils.error.try_external_errors.try_manage_strict_path_resolving(path_to_resolve=vcvars_arch_batch_file,
                                                                         external_errors_to_manage={(Exception,): utils.error.cls_def.MSVCCompilerVcvarsBatchFileNotFoundError})

        return vcvars_arch_batch_file

    def __get_vcvars_dir(self) -> Path:
        vcvars_dir: Path = self.installation_dir / self.get_vcvars_dir_relative_to_installation_dir()

        utils.error.try_external_errors.try_manage_strict_path_resolving(path_to_resolve=vcvars_dir,
                                                                         external_errors_to_manage={(Exception,): utils.error.cls_def.MSVCCompilerVcvarsDirNotFoundError})

        return vcvars_dir

    def __compute_vcvars_arch_batch_filename(self) -> str:
        return self.get_vcvars_prefix() + str(self.arch.value) + self.get_vcvars_extension()
