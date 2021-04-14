import os
import pathlib
import typing

T_PathLike_Constraints: typing.Final = (pathlib.Path, os.PathLike, str, bytes)
T_AnyPath_Constraints: typing.Final = (pathlib.Path, os.PathLike, str, bytes, type(None))

PathLike: typing.Final[type] = typing.Union[*T_PathLike_Constraints, ...]
AnyPath: typing.Final[type] = typing.Union[*T_AnyPath_Constraints, ...]

T_PathLike: typing.Final[type] = typing.TypeVar("T_PathLike", *T_PathLike_Constraints, ...)
T_AnyPath: typing.Final[type] = typing.TypeVar("T_AnyPath", *T_AnyPath_Constraints, ...)
