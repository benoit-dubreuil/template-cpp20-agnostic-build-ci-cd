from typing import Optional, Union

from .cls_mixin import *
from utils.meta_prog.encapsulation import *


@export
class GenericClassProxyInjectorMixin(GenericClassMixin):
    from .cls_proxy import *

    __TAlias_Generics_Subscript_Op = Optional[Union[tuple, type]]

    def __init__(self,
                 *args,
                 generics_by_type_vars: TAlias_Generics_By_TypeVars = None,
                 **kwargs) -> None:
        if generics_by_type_vars is None:
            generic_cls = type(self)
            generics = tuple()
            cls_proxy = GenericClassProxy(generic_cls=generic_cls, generics=generics)

            generics_by_type_vars = cls_proxy.generics_by_type_vars

        super().__init__(*args, generics_by_type_vars=generics_by_type_vars, **kwargs)

    @classmethod
    def __class_getitem__(cls, item: __TAlias_Generics_Subscript_Op):
        generics = item if isinstance(item, tuple) else (item,)
        return GenericClassProxy(generic_cls=cls, generics=generics)
