import pathlib
import typing
import os

AnyPath = typing.TypeVar("AnyPath", pathlib.Path, os.PathLike, str, bytes, type(None))
