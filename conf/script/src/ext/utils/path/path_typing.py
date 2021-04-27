__all__ = ['TConstraints_PathLike',
           'TConstraints_AnyPath',
           'PathLike',
           'AnyPath',
           'T_PathLike',
           'T_AnyPath']

import os
from pathlib import Path
from typing import TypeVar, Union

TConstraints_PathLike = (Path, os.PathLike, str, bytes)
TConstraints_AnyPath = (Path, os.PathLike, str, bytes, type(None))

PathLike = Union[Path, os.PathLike, str, bytes]
AnyPath = Union[Path, os.PathLike, str, bytes, type(None)]

T_PathLike = TypeVar("T_PathLike", Path, os.PathLike, str, bytes)
T_AnyPath = TypeVar("T_AnyPath", Path, os.PathLike, str, bytes, type(None))