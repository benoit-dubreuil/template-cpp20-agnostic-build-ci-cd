from typing import Generic

from utils.meta_prog.encapsulation import *
from utils.meta_prog.introspection import *
from .cls_mixin import *

__all__: TAlias_Macro_All = ['TAlias_generic_cls']

TAlias_generic_cls = type[Generic]


@export
class GenericClassWrapperDataMixin:
    TAlias_generic_cls = type[Generic]

    wrapped_generic_cls: Final[TAlias_generic_cls]

    def __init__(self, generic_cls: TAlias_generic_cls, *args, **kwargs) -> None:
        self.wrapped_generic_cls = generic_cls
        super().__init__(*args, **kwargs)
