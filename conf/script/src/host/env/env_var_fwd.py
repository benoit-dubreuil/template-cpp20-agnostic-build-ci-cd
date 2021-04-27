__all__ = ['T_EnvVar',
           'T_Env_Key',
           'T_Env_Single_Val']

from typing import AnyStr, TypeVar

from ext.utils.path import *

T_EnvVar = TypeVar('T_EnvVar', bound='EnvVar')

T_Env_Key = AnyStr
T_Env_Single_Val = T_PathLike
