from utils.meta_prog.generics.mixin import GenericClassMixin
from utils.meta_prog.generics.proxy import GenericClassProxy


class GenericClassProxyInjectorMixin(GenericClassMixin):

    @classmethod
    def __class_getitem__(cls, item: tuple):
        return GenericClassProxy(generic_cls=cls, generics=item)
