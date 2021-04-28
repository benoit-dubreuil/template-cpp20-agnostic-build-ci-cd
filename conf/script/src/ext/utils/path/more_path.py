__all__ = ['is_dir_empty',
           'cast_path_like']

from pathlib import Path
from typing import cast

from .path_typing import *
from ..string import *


def is_dir_empty(dir_path: Path) -> bool:
    return not any(dir_path.iterdir())


def cast_path_like(target_cls: type[T_PathLike], src_path_like: TUnion_PathLike, encoding: str = UTF_8) -> T_PathLike:
    casted_path_like: T_PathLike

    if isinstance(src_path_like, target_cls):
        casted_path_like = cast(target_cls, src_path_like)
    elif issubclass(target_cls, Path):
        casted_path_like = target_cls(src_path_like)
    else:
        casted_path_like = target_cls(src_path_like, encoding)

    return casted_path_like
