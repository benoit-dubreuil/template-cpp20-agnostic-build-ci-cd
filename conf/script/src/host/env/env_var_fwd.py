import abc
import collections.abc
import typing

import utils.more_typing

T_Key: typing.Final[type] = utils.more_typing.T_PathLike
T_Single_Value: typing.Final[type] = utils.more_typing.T_PathLike
T_Values: typing.Final[type] = list[T_Single_Value]


# Forward declaration
class EnvVarSingleIt(collections.abc.Iterator[utils.more_typing.T_PathLike], metaclass=abc.ABCMeta):
    pass


# Forward declaration
class EnvVarKeyIt(EnvVarSingleIt, metaclass=abc.ABCMeta):
    pass


# Forward declaration
class EnvVarJoinedValues(collections.abc.Iterator[T_Single_Value], metaclass=abc.ABCMeta):
    pass
