import dataclasses
import pathlib
import typing

import build_system.build_target.name


@dataclasses.dataclass(order=True)
class BuildTarget:
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
