from typing import *

from macro import *

__all__: TAlias_Macro_All = ['get_or_create_attr', 'get_or_create_optional_attr']

T_Attr_Val = TypeVar('T_Attr_Val')


def get_or_create_attr(obj, attr: str, default_val: Optional[T_Attr_Val] = None) -> T_Attr_Val:
    attr_val: T_Attr_Val

    assert hasattr(obj, Macro.DICT)

    if not hasattr(obj, attr):
        non_none_default_val: T_Attr_Val

        if default_val is None:
            non_none_default_val = T_Attr_Val()
        else:
            non_none_default_val = default_val

        attr_val = non_none_default_val
        setattr(obj, attr, attr_val)
    else:
        attr_val = getattr(obj, attr)

    return attr_val


def get_or_create_optional_attr(obj, attr: str, default_val: Optional[T_Attr_Val] = None) -> Optional[T_Attr_Val]:
    attr_val: Optional[T_Attr_Val]

    assert hasattr(obj, Macro.DICT)

    if not hasattr(obj, attr):
        attr_val = default_val
        setattr(obj, attr, attr_val)
    else:
        attr_val = getattr(obj, attr)

    return attr_val
