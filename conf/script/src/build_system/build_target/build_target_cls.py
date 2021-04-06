import dataclasses
import pathlib
import typing

import build_system.build_target.name
import build_system.build_target.build_type
import build_system.compiler.host.architecture
import build_system.compiler.installed_instance


@dataclasses.dataclass(order=True)
class BuildTarget:
    compiler_instance: build_system.compiler.installed_instance.CompilerInstance
    target_build_type: build_system.build_target.build_type.TargetBuildType

    name: typing.Final[build_system.build_target.name.TargetBuildName]
    dir: typing.Optional[pathlib.Path]

    def __init__(self, build_name: build_system.build_target.name.TargetBuildName) -> None:
        self.name = build_name
        self.dir = None

    def __str__(self) -> str:
        return self.form_name()

    def form_name(self):
        return str(self.name)

    def compute_target_build_dir(self, project_build_dir: pathlib.Path):
        self.dir = project_build_dir / self.form_name()

    def get_build_type(self) -> build_system.build_target.build_type.TargetBuildType:
        return self.name.target_build_type

    @staticmethod
    def get_name_separator() -> str:
        return '-'
