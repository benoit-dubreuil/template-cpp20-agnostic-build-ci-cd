__all__ = ['TAlias_generic_cls']

from typing import Final, Generic

from ..encapsulation import *
from ..introspection import *
from .cls_mixin import *

TAlias_generic_cls = type[Generic]


@export
class GenericClassWrapperDataMixin:
    wrapped_generic_cls: Final[TAlias_generic_cls]

    def __init__(self, generic_cls: TAlias_generic_cls, *args, **kwargs) -> None:
        self.wrapped_generic_cls = generic_cls
        super().__init__(*args, **kwargs)
