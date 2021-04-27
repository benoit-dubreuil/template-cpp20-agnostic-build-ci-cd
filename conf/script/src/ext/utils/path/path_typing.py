__all__ = ['TUnion_PathLike',
           'TUnion_AnyPath',
           'T_PathLike',
           'T_AnyPath']

import os
from pathlib import Path
from typing import TypeVar, Union

from ..string import *

TUnion_PathLike = Union[Path, os.PathLike, TUnion_AnyStr]
TUnion_AnyPath = Union[Path, os.PathLike, TUnion_AnyStr, type(None)]

T_PathLike = TypeVar("T_PathLike", Path, os.PathLike, TUnion_AnyStr)
T_AnyPath = TypeVar("T_AnyPath", Path, os.PathLike, TUnion_AnyStr, type(None))
