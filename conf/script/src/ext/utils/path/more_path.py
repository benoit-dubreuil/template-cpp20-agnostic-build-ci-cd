__all__ = ['is_dir_empty',
           'cast_path_like']

from pathlib import Path
from typing import cast

from .path_typing import *
from ..string import *


def is_dir_empty(dir_path: Path) -> bool:
    return not any(dir_path.iterdir())


def cast_path_like(target_cls: type[T_PurePathLike], src_path_like: TUnion_PathLike, encoding: str = UTF_8) -> T_PurePathLike:
    casted_path_like: T_PurePathLike

    if isinstance(src_path_like, target_cls):
        casted_path_like = cast(target_cls, src_path_like)
    elif issubclass(target_cls, Path):
        casted_path_like = target_cls(src_path_like)
    else:
        if isinstance(src_path_like, Path):
            src_path_like = str(src_path_like)

        casted_path_like = cast_any_str(target_cls=target_cls, src_any_str=src_path_like, encoding=encoding)

    return casted_path_like
