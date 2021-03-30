import pathlib
import typing
import os

PathLike = typing.TypeVar("PathLike", pathlib.Path, os.PathLike, str, bytes)
AnyPath = typing.TypeVar("AnyPath", pathlib.Path, os.PathLike, str, bytes, type(None))
