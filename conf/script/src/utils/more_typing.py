import os
import pathlib
import typing

from .meta_prog.introspection import *

__all__: TAlias_Macro_All = ['TConstraints_PathLike', 'TConstraints_AnyPath',
                             'PathLike', 'AnyPath',
                             'T_PathLike', 'T_AnyPath']

TConstraints_PathLike = (pathlib.Path, os.PathLike, str, bytes)
TConstraints_AnyPath = (pathlib.Path, os.PathLike, str, bytes, type(None))

PathLike = typing.Union[pathlib.Path, os.PathLike, str, bytes]
AnyPath = typing.Union[pathlib.Path, os.PathLike, str, bytes, type(None)]

T_PathLike = typing.TypeVar("T_PathLike", pathlib.Path, os.PathLike, str, bytes)
T_AnyPath = typing.TypeVar("T_AnyPath", pathlib.Path, os.PathLike, str, bytes, type(None))
