__all__ = ['cast_any_str']

from typing import AnyStr, Union


def cast_any_str(target_cls: type[AnyStr], src_any_str: Union[str, bytes], encoding: str = 'utf-8') -> AnyStr:
    """
    Casts an AnyStr into the supplied target AnyStr concrete class.

    A new instance is always returned, even if the source AnyStr object's class and the target AnyStr concrete class are the same.
    """

    casted_any_str: AnyStr

    if isinstance(src_any_str, target_cls):
        casted_any_str = target_cls(src_any_str)
    else:
        casted_any_str = target_cls(src_any_str, encoding)

    return casted_any_str
