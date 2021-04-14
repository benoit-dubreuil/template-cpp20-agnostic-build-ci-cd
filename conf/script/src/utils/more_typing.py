import os
import pathlib
import typing

T_PathLike_Constraints: typing.Final = (pathlib.Path, os.PathLike, str, bytes)
T_AnyPath_Constraints: typing.Final = (pathlib.Path, os.PathLike, str, bytes, type(None))

PathLike: typing.Final[type] = typing.Union[pathlib.Path, os.PathLike, str, bytes]
AnyPath: typing.Final[type] = typing.Union[pathlib.Path, os.PathLike, str, bytes, type(None)]

T_PathLike: typing.Final[type] = typing.TypeVar("T_PathLike", pathlib.Path, os.PathLike, str, bytes)
T_AnyPath: typing.Final[type] = typing.TypeVar("T_AnyPath", pathlib.Path, os.PathLike, str, bytes, type(None))
