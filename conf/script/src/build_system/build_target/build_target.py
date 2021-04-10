import dataclasses
import pathlib
from typing import Final, Optional

import build_system.compiler.build_option.build_type
import build_system.compiler.build_option.sanitizer
import build_system.compiler.installed_instance


@dataclasses.dataclass(order=True)
class BuildTarget:
    compiler_instance: Final[build_system.compiler.installed_instance.CompilerInstance]
    target_build_type: Final[build_system.compiler.build_option.build_type.TargetBuildType]
    sanitizer: Final[build_system.compiler.build_option.sanitizer.CompilerSanitizer]

    dir: Optional[pathlib.Path]

    def __init__(self,
                 compiler_instance: build_system.compiler.installed_instance.CompilerInstance,
                 target_build_type: build_system.compiler.build_option.build_type.TargetBuildType,
                 sanitizer: build_system.compiler.build_option.sanitizer.CompilerSanitizer = build_system.compiler.build_option.sanitizer.CompilerSanitizer.NONE) \
            -> None:
        self.compiler_instance = compiler_instance
        self.target_build_type = target_build_type
        self.sanitizer = sanitizer

        self.dir = None

    def form_name(self):
        return str(self)

    @staticmethod
    def get_name_separator() -> str:
        return '-'

    def __str__(self) -> str:
        sep: Final[str] = self.get_name_separator()

        os_family_name = self.compiler_instance.os_family.value
        arch_bit_name = self.compiler_instance.arch.arch_to_bit_name()
        compiler_name = self.compiler_instance.compiler_family.value
        compiler_version_name = str(self.compiler_instance.version)
        target_build_type_name = self.target_build_type.value
        sanitizer_name = self.sanitizer.value + sep + 'san'

        return os_family_name + sep + arch_bit_name + sep + compiler_name + sep + compiler_version_name + sep + target_build_type_name + sep + sanitizer_name
