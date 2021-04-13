from dataclasses import dataclass

from utils.more_typing import PathLike


@dataclass(init=False, order=True)
class EnvVar:
    key_name: PathLike
    values: list[PathLike]

    def __init__(self, key_name=None, values=None) -> None:
        self.key_name = key_name if key_name is not None else str()
        self.values = values if values is not None else []
