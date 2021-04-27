__all__ = ['TConstraints_PathLike',
           'TConstraints_AnyPath',
           'TUnion_PathLike',
           'TUnion_AnyPath',
           'T_PathLike',
           'T_AnyPath']

import os
from pathlib import Path
from typing import TypeVar, Union

TConstraints_PathLike = (Path, os.PathLike, str, bytes)
TConstraints_AnyPath = (Path, os.PathLike, str, bytes, type(None))

TUnion_PathLike = Union[Path, os.PathLike, str, bytes]
TUnion_AnyPath = Union[Path, os.PathLike, str, bytes, type(None)]

T_PathLike = TypeVar("T_PathLike", Path, os.PathLike, str, bytes)
T_AnyPath = TypeVar("T_AnyPath", Path, os.PathLike, str, bytes, type(None))
