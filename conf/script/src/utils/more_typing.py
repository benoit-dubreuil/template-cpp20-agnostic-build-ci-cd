import pathlib
import typing

AnyPath = typing.TypeVar("AnyPath", pathlib.Path, str, bytes, type(None))
