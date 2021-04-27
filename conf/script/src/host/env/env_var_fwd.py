__all__ = ['T_EnvVar',
           'T_Key',
           'T_Single_Value']

from typing import AnyStr, TypeVar

from ext.utils.path import *

T_EnvVar = TypeVar('T_EnvVar', bound='EnvVar')

T_Key = AnyStr
T_Single_Value = T_PathLike
