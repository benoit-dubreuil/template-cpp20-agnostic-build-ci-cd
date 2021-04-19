from typing import *
from macro import *

T_Attr_Val = TypeVar('T_Attr_Val')


def get_or_create_optional_attr(obj, attr: str, default_val: Optional[T_Attr_Val] = None) -> Optional[T_Attr_Val]:
    attr_val: Optional[T_Attr_Val]

    assert hasattr(obj, Macro.DICT)

    if not hasattr(obj, attr):
        attr_val = default_val
        setattr(obj, attr, attr_val)
    else:
        attr_val = getattr(obj, attr)

    return attr_val
