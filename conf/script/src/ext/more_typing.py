import os
from pathlib import Path
from typing import TypeVar, Union

from .meta_prog.introspection import *

__all__: TAlias_Macro_All = ['TConstraints_PathLike', 'TConstraints_AnyPath',
                             'PathLike', 'AnyPath',
                             'T_PathLike', 'T_AnyPath']

TConstraints_PathLike = (Path, os.PathLike, str, bytes)
TConstraints_AnyPath = (Path, os.PathLike, str, bytes, type(None))

PathLike = Union[Path, os.PathLike, str, bytes]
AnyPath = Union[Path, os.PathLike, str, bytes, type(None)]

T_PathLike = TypeVar("T_PathLike", Path, os.PathLike, str, bytes)
T_AnyPath = TypeVar("T_AnyPath", Path, os.PathLike, str, bytes, type(None))
