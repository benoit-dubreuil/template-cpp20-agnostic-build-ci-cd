import dataclasses
import pathlib
from typing import Final, Optional

import build_system.build_target.build_type
import build_system.compiler.host.architecture
import build_system.compiler.installed_instance


@dataclasses.dataclass(order=True)
class BuildTarget:
    compiler_instance: build_system.compiler.installed_instance.CompilerInstance
    target_build_type: build_system.build_target.build_type.TargetBuildType

    dir: Optional[pathlib.Path]

    def __init__(self,
                 compiler_instance: build_system.compiler.installed_instance.CompilerInstance,
                 target_build_type: build_system.build_target.build_type.TargetBuildType) -> None:
        self.compiler_instance = compiler_instance
        self.target_build_type = target_build_type
        self.dir = None

    def form_name(self):
        return str(self)

    def compute_target_build_dir(self, project_build_dir: pathlib.Path):
        self.dir = project_build_dir / self.form_name()

    def get_build_type(self) -> build_system.build_target.build_type.TargetBuildType:
        return self.target_build_type

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

        return os_family_name + sep + arch_bit_name + sep + compiler_name + sep + compiler_version_name + sep + target_build_type_name
