import os
from dataclasses import dataclass

from utils.more_typing import PathLike


@dataclass(init=False, order=True)
class EnvVar:
    key_name: PathLike
    values: list[PathLike]

    def __init__(self, key_name=None, values=None) -> None:
        self.key_name = key_name if key_name is not None else str()
        self.values = values if values is not None else []

    def join_values(self) -> str:
        return os.pathsep.join(self.values)

    def __str__(self) -> str:
        assert self.key_name is not None
        assert self.values is not None

        joined_values = self.join_values()

        return f'{self.key_name}={joined_values}'
