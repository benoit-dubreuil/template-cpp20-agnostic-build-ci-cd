__all__ = ['GenericClassProxyInjectorMixin']

from typing import Optional, Union

from .cls_mixin import *
from .cls_proxy import *
from .data import *


class GenericClassProxyInjectorMixin(GenericClassMixin):
    __TAlias_Generics_Subscript_Op = Optional[Union[tuple, type]]

    def __new__(cls,
                *args,
                generics_by_type_vars: TAlias_Generics_By_TypeVars = None,
                **kwargs):
        if generics_by_type_vars is None:
            generic_cls = cls
            generics: tuple[type] = tuple()
            cls_proxy = GenericClassProxy(generic_cls=generic_cls, generics=generics)

            generics_by_type_vars = cls_proxy.generics_by_type_vars

        return super().__new__(cls, *args, generics_by_type_vars=generics_by_type_vars, **kwargs)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @classmethod
    def __class_getitem__(cls, key: __TAlias_Generics_Subscript_Op):
        generics = key if isinstance(key, tuple) else (key,)
        return GenericClassProxy(generic_cls=cls, generics=generics)
