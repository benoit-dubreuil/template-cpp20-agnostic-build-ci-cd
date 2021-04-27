__all__ = ['T_EnvVar',
           'T_Key',
           'T_Single_Value']

import typing

import utils.more_typing

T_EnvVar = typing.TypeVar('T_EnvVar', bound='EnvVar')

T_Key = typing.AnyStr
T_Single_Value = utils.more_typing.T_PathLike
