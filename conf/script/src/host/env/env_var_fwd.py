import typing

import utils.more_typing

T_Key: typing.Final[type] = typing.AnyStr
T_Single_Value: typing.Final[type] = utils.more_typing.T_PathLike
T_Values: typing.Final[type] = list[T_Single_Value]
