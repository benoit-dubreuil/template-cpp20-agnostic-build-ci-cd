import abc
import collections.abc
import typing

import utils.more_typing

_T_Key: typing.Final[type] = utils.more_typing.T_PathLike
_T_Single_Value: typing.Final[type] = utils.more_typing.T_PathLike
_T_Values = typing.Final[list[_T_Single_Value]]


# Forward declaration
class _EnvVarKeyIt(collections.abc.Iterator[_T_Key], metaclass=abc.ABCMeta):
    pass


# Forward declaration
class _EnvVarValuesIt(collections.abc.Iterator[_T_Values], metaclass=abc.ABCMeta):
    pass


# Forward declaration
class _EnvVarJoinedValues(collections.abc.Iterator[_T_Single_Value], metaclass=abc.ABCMeta):
    pass
