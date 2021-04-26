__all__ = ['GNUCompilerInstance']

import contextlib
from dataclasses import dataclass
from pathlib import Path

from error import *
from error.utils import *
from ext.utils.cmd_integrity import *
from .compiler_instance import *
from ..build_option import *
from ..core import *


@dataclass(order=True, frozen=True)
class GNUCompilerInstance(CompilerInstance):
    executable_file: Path

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        object.__setattr__(self, 'executable_file', self.__get_executable_file_from_installation_dir())

    def __get_executable_file_from_installation_dir(self) -> Path:
        executable_file, exists = get_cmd_path(cmd=self.compiler_family.value, dir_path=self.installation_dir)

        if not exists:
            raise CompilerNotFoundError()

        try_manage_strict_path_resolving(path_to_resolve=executable_file,
                                         external_errors_to_manage={(Exception,): CompilerNotFoundError})

        return executable_file

    def create_env_context_manager(self) -> contextlib.AbstractContextManager:
        import build_system.compiler.installed_instance.set_env_default_compiler
        return build_system.compiler.installed_instance.set_env_default_compiler.EnvDefaultCompiler(compiler=self)

    @classmethod
    def _find_installation_dir_by_compiler_family(cls, compiler_family: CompilerFamily) -> Path:
        cls._assert_compiler_family(compiler_family=compiler_family)

        compiler_location, compiler_instance_exists = get_cmd_path(cmd=compiler_family.value)

        if not compiler_instance_exists:
            raise CompilerNotFoundError()

        compiler_installation_dir = compiler_location.parent

        return compiler_installation_dir

    @staticmethod
    def get_supported_compiler_families() -> list[CompilerFamily]:
        return [CompilerFamily.GCC,
                CompilerFamily.CLANG]

    @staticmethod
    def get_supported_sanitizers() -> list[CompilerSanitizer]:
        return list(CompilerSanitizer)
