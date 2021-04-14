import typing
import utils.more_typing

T_EnvVar = typing.TypeVar('T_EnvVar', bound='EnvVar')

T_Key: typing.Final[type] = typing.AnyStr

T_Single_Value: typing.Final[type] = utils.more_typing.T_PathLike
T_Values_Collection: typing.Final[type[typing.Generic]] = list

T_Values: typing.Final[type] = T_Values_Collection[T_Single_Value]
T_Default_AnyStr: typing.Final[type] = str
