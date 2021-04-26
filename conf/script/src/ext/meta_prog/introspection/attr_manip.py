__all__ = ['get_or_create_attr']

from typing import Callable, TypeVar

from .macro import *

_T_Attr_Val = TypeVar('_T_Attr_Val')
_TAlias_Attr_Val_Generator = Callable[[], _T_Attr_Val]


def get_or_create_attr(obj,
                       attr: str,
                       default_val_generator: _TAlias_Attr_Val_Generator = lambda: _T_Attr_Val()) -> _T_Attr_Val:
    attr_val: _T_Attr_Val

    assert hasattr(obj, Macro.DICT)

    if not hasattr(obj, attr):
        attr_val = default_val_generator()
        setattr(obj, attr, attr_val)
    else:
        attr_val = getattr(obj, attr)

    return attr_val
