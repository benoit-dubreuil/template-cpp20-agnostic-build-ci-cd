__all__ = ['T_EnvVar',
           'T_Key',
           'T_Single_Value']

import typing

from ext.utils.path import *

T_EnvVar = typing.TypeVar('T_EnvVar', bound='EnvVar')

T_Key = typing.AnyStr
T_Single_Value = T_PathLike
