__all__ = ['MSVCCompilerInstance']

import contextlib
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, final

from ..core import *
from ..build_option import *
from .compiler_instance import *
from build_system.cmd.compiler.host.get_info.location.msvc import *
from ext.error import *
from ext.error.utils import *


@final
@dataclass(order=True, frozen=True)
class MSVCCompilerInstance(CompilerInstance):
    vcvars_arch_batch_file: Path
    cached_compiler_env: Optional[dict[str, list[str]]]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        object.__setattr__(self, 'vcvars_arch_batch_file', self.__find_vcvars_batch_file())

    @classmethod
    def _find_installation_dir_by_compiler_family(cls, compiler_family: CompilerFamily) -> Path:
        cls._assert_compiler_family(compiler_family=compiler_family)

        compiler_installation_dir = find_msvc_location()
        return compiler_installation_dir

    @staticmethod
    def get_supported_compiler_families() -> list[CompilerFamily]:
        return [CompilerFamily.MSVC]

    @staticmethod
    def get_supported_sanitizers() -> list[CompilerSanitizer]:
        return [CompilerSanitizer.NONE,
                CompilerSanitizer.ADDRESS]

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
        import set_env_msvc
        return set_env_msvc.EnvMSVC(compiler=self)

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

    def cache_vcvars_as_compiler_env(self, vcvars: dict[str, list[str]]) -> None:
        object.__setattr__(self, 'cached_compiler_env', vcvars)

    def has_cached_compiler_env(self) -> bool:
        return self.cached_compiler_env is not None

    def __find_vcvars_batch_file(self) -> Path:
        vcvars_dir: Path = self.__get_vcvars_dir()
        vcvars_filename: str = self.__compute_vcvars_arch_batch_filename()
        vcvars_arch_batch_file = vcvars_dir / vcvars_filename
        vcvars_arch_batch_file = vcvars_arch_batch_file.absolute()

        try_manage_strict_path_resolving(path_to_resolve=vcvars_arch_batch_file,
                                         external_errors_to_manage={
                                             (Exception,): MSVCCompilerVcvarsBatchFileNotFoundError})

        return vcvars_arch_batch_file

    def __get_vcvars_dir(self) -> Path:
        vcvars_dir: Path = self.installation_dir / self.get_vcvars_dir_relative_to_installation_dir()

        try_manage_strict_path_resolving(path_to_resolve=vcvars_dir,
                                         external_errors_to_manage={(Exception,): MSVCCompilerVcvarsDirNotFoundError})

        return vcvars_dir

    def __compute_vcvars_arch_batch_filename(self) -> str:
        return self.get_vcvars_prefix() + str(self.arch.value) + self.get_vcvars_extension()
