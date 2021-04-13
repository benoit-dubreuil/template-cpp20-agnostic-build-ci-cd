import os
import pathlib
import typing

PathLike = typing.Union[pathlib.Path, os.PathLike, str, bytes]
AnyPath = typing.Union[pathlib.Path, os.PathLike, str, bytes, type(None)]

T_PathLike = typing.TypeVar("T_PathLike", pathlib.Path, os.PathLike, str, bytes)
T_AnyPath = typing.TypeVar("T_AnyPath", pathlib.Path, os.PathLike, str, bytes, type(None))
