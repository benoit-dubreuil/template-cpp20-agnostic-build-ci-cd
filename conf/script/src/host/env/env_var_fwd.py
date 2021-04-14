import typing

import utils.more_typing

TAlias_Default_AnyStr: typing.Final[type] = str

T_EnvVar = typing.TypeVar('T_EnvVar', bound='EnvVar')

T_Key: typing.Final[type] = typing.AnyStr

T_Single_Value: typing.Final[type] = utils.more_typing.T_PathLike
TAlias_Values: typing.Final[type] = list[T_Single_Value]
