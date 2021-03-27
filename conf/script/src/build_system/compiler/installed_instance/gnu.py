from dataclasses import dataclass
from pathlib import Path

import build_system.compiler.family
import build_system.compiler.installed_instance.compiler_instance
import utils.cmd_integrity
import utils.error.cls_def


@dataclass(order=True, frozen=True)
class GNUCompilerInstance(build_system.compiler.installed_instance.compiler_instance.CompilerInstance):
    executable_file: Path

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        object.__setattr__(self, 'executable_file', self.__get_executable_file_from_installation_dir())

    def __get_executable_file_from_installation_dir(self) -> Path:
        executable_file, exists = utils.cmd_integrity.get_cmd_path(cmd=self.compiler_family.value, dir_path=self.installation_dir)

        if not exists:
            raise utils.error.cls_def.CompilerNotFoundError()

        try:
            executable_file.resolve(strict=True)

        except Exception as raised_error:
            supported_exception = utils.error.cls_def.CompilerNotFoundError()
            supported_exception.with_traceback(raised_error.__traceback__)

            raise supported_exception

        return executable_file

    @classmethod
    def _find_installation_dir_by_compiler_family(cls, compiler_family: build_system.compiler.family.CompilerFamily) -> Path:
        cls._assert_compiler_family(compiler_family=compiler_family)

        compiler_location, compiler_instance_exists = utils.cmd_integrity.get_cmd_path(cmd=compiler_family.value)

        if not compiler_instance_exists:
            raise utils.error.cls_def.CompilerNotFoundError()

        compiler_installation_dir = compiler_location.parent

        return compiler_installation_dir

    @staticmethod
    def get_supported_compiler_families() -> list[build_system.compiler.family.CompilerFamily]:
        return [build_system.compiler.family.CompilerFamily.GCC,
                build_system.compiler.family.CompilerFamily.CLANG]
