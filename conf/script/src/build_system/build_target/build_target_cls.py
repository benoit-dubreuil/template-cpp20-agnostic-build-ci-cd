import dataclasses
import pathlib
import typing

import build_system.build_target.name


@dataclasses.dataclass(order=True, frozen=True)
class BuildTarget:
    build_name: build_system.build_target.name.TargetBuildName
    build_dir: typing.Optional[pathlib.Path]

    def __str__(self) -> str:
        return str(self.build_name)
