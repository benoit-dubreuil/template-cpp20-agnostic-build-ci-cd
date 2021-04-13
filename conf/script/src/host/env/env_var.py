from dataclasses import dataclass

from utils.more_typing import PathLike


@dataclass(init=False, order=True)
class EnvVar:
    key_name: PathLike
    values: list[PathLike]
