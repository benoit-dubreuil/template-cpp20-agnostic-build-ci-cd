__all__ = ['T_Env_Key',
           'T_Env_Single_Val',
           'TAlias_Env_Values']

from typing import AnyStr, TypeVar

from ext.utils.path import *

T_Env_Key = AnyStr
T_Env_Single_Val = T_PurePathLike

TAlias_Env_Values = list[T_Env_Single_Val]
