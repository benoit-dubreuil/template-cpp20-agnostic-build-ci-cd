__all__ = ['cast_any_str']

from typing import AnyStr, cast

from .encoding_names import *
from .str_typing import *


def cast_any_str(target_cls: type[AnyStr], src_any_str: TUnion_AnyStr, encoding: str = UTF_8) -> AnyStr:
    casted_any_str: AnyStr

    if isinstance(src_any_str, target_cls):
        casted_any_str = cast(target_cls, src_any_str)
    else:
        casted_any_str = target_cls(src_any_str, encoding)

    return casted_any_str
