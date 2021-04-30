__all__ = ['TUnion_PurePath',
           'TUnion_PurePathLike',
           'TUnion_AnyPurePath',
           'TUnion_Path',
           'TUnion_PathLike',
           'TUnion_AnyPath',
           'T_PurePath',
           'T_PurePathLike',
           'T_AnyPurePath',
           'T_Path',
           'T_PathLike',
           'T_AnyPath']

import os
from pathlib import Path, PurePath
from typing import TypeVar, Union

from ..string import *

TUnion_PurePath = Union[PurePath, os.PathLike]
TUnion_PurePathLike = Union[TUnion_PurePath, TUnion_AnyStr]
TUnion_AnyPurePath = Union[TUnion_PurePathLike, type(None)]

TUnion_Path = Union[Path, os.PathLike]
TUnion_PathLike = Union[TUnion_Path, TUnion_AnyStr]
TUnion_AnyPath = Union[TUnion_PathLike, type(None)]

T_PurePath = TypeVar("T_PurePath", PurePath, os.PathLike)
T_PurePathLike = TypeVar("T_PurePathLike", PurePath, os.PathLike, str, bytes)
T_AnyPurePath = TypeVar("T_AnyPurePath", PurePath, os.PathLike, str, bytes, type(None))

T_Path = TypeVar("T_Path", Path, os.PathLike)
T_PathLike = TypeVar("T_PathLike", Path, os.PathLike, str, bytes)
T_AnyPath = TypeVar("T_AnyPath", Path, os.PathLike, str, bytes, type(None))
