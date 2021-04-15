import typing

import utils.meta_prog.generics.cls_mixin
import utils.meta_prog.generics.cls_proxy


class GenericClassProxyInjectorMixin(utils.meta_prog.generics.cls_mixin.GenericClassMixin):
    __TAlias_Generics_Subscript_Op = typing.Optional[typing.Union[tuple, type]]

    def __init__(self,
                 *args,
                 generics_by_type_vars: utils.meta_prog.generics.cls_mixin.GenericClassMixin.TAlias_Generics_By_TypeVars = None,
                 **kwargs) -> None:
        if generics_by_type_vars is None:
            generic_cls = type(self)
            generics = tuple()
            cls_proxy = utils.meta_prog.generics.cls_proxy.GenericClassProxy(generic_cls=generic_cls, generics=generics)

            generics_by_type_vars = cls_proxy.generics_by_type_vars

        super().__init__(*args, generics_by_type_vars=generics_by_type_vars, **kwargs)

    @classmethod
    def __class_getitem__(cls, item: __TAlias_Generics_Subscript_Op):
        generics = item if isinstance(item, tuple) else (item,)
        return utils.meta_prog.generics.cls_proxy.GenericClassProxy(generic_cls=cls, generics=generics)
