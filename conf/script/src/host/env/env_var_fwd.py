import abc
import collections.abc
import typing

import utils.more_typing

T_ItValue: typing.Final[type] = typing.TypeVar(name='T_ItValue', utils.more_typing.T_PathLike.)
T_Key: typing.Final[type] = utils.more_typing.T_PathLike
T_Single_Value: typing.Final[type] = utils.more_typing.T_PathLike
T_Values = typing.Final[list[T_Single_Value]]


# Forward declaration
class EnvVarKeyIt(collections.abc.Iterator[T_Key], metaclass=abc.ABCMeta):
    pass


# Forward declaration
class EnvVarValuesIt(collections.abc.Iterator[T_Values], metaclass=abc.ABCMeta):
    pass


# Forward declaration
class EnvVarJoinedValues(collections.abc.Iterator[T_Single_Value], metaclass=abc.ABCMeta):
    pass
