import typing

import utils.meta_prog.generics.cls_mixin
import utils.meta_prog.generics.cls_proxy


class GenericClassProxyInjectorMixin(utils.meta_prog.generics.cls_mixin.GenericClassMixin):
    __TAlias_Generics_Subscript_Op = typing.Optional[typing.Union[tuple, type]]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @classmethod
    def __class_getitem__(cls, item: __TAlias_Generics_Subscript_Op):
        generics = item if isinstance(item, tuple) else (item,)
        return utils.meta_prog.generics.cls_proxy.GenericClassProxy(generic_cls=cls, generics=generics)
