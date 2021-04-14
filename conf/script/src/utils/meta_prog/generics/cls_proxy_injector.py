import utils.meta_prog.generics.cls_mixin
import utils.meta_prog.generics.cls_proxy


class GenericClassProxyInjectorMixin(utils.meta_prog.generics.cls_mixin.GenericClassMixin):

    @classmethod
    def __class_getitem__(cls, item: tuple):
        generics = item if isinstance(item, tuple) else (item,)
        return utils.meta_prog.generics.cls_proxy.GenericClassProxy(generic_cls=cls, generics=generics)
