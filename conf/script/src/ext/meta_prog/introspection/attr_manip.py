from typing import Callable, TypeVar

from .macro import *

__all__: TAlias_Macro_All = ['get_or_create_attr']

T_Attr_Val = TypeVar('T_Attr_Val')
TAlias_Attr_Val_Generator = Callable[[], T_Attr_Val]


def get_or_create_attr(obj,
                       attr: str,
                       default_val_generator: TAlias_Attr_Val_Generator = lambda: T_Attr_Val()) -> T_Attr_Val:
    attr_val: T_Attr_Val

    assert hasattr(obj, Macro.DICT)

    if not hasattr(obj, attr):
        attr_val = default_val_generator()
        setattr(obj, attr, attr_val)
    else:
        attr_val = getattr(obj, attr)

    return attr_val
