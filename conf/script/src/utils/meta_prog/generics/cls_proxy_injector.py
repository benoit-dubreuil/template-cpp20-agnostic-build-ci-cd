import utils.meta_prog.generics.cls_mixin
import utils.meta_prog.generics.cls_proxy
import typing


class GenericClassProxyInjectorMixin(utils.meta_prog.generics.cls_mixin.GenericClassMixin):
    __TAlias_Generics_Subscript_Op = typing.Optional[typing.Union[tuple, type]]

    @classmethod
    def __class_getitem__(cls, item: __TAlias_Generics_Subscript_Op):
        generics = item if isinstance(item, tuple) else (item,)
        return utils.meta_prog.generics.cls_proxy.GenericClassProxy(generic_cls=cls, generics=generics)
