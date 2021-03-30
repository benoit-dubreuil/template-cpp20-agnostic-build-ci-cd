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
        return str(self.name)
