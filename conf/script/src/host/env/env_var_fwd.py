import typing

import utils.more_typing

TAlias_Default_AnyStr = str

T_EnvVar = typing.TypeVar('T_EnvVar', bound='EnvVar')

T_Key = typing.AnyStr
T_Single_Value = utils.more_typing.T_PathLike
