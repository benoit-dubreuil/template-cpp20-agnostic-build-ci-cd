import utils.meta_prog.generics.cls_wrapper_data


class GenericClassWrapperMixin(utils.meta_prog.generics.cls_wrapper_data.GenericClassWrapperDataMixin):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @property
    def __class__(self) -> utils.meta_prog.generics.cls_wrapper_data.GenericClassWrapperDataMixin.TAlias_generic_cls:
        proxy_cls = self.wrapped_generic_cls if hasattr(self, 'wrapped_generic_cls') else super().__class__()
        return proxy_cls
