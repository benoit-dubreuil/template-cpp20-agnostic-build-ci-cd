import os
import pathlib
import typing

PathLike = typing.TypeVar("PathLike", pathlib.Path, os.PathLike, str, bytes)
AnyPath = typing.TypeVar("AnyPath", pathlib.Path, os.PathLike, str, bytes, type(None))
