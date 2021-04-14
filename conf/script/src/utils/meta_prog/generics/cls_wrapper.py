import utils.meta_prog.generics.cls_wrapper_data


class GenericClassWrapperMixin(utils.meta_prog.generics.cls_wrapper_data.GenericClassWrapperDataMixin):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @property
    def __class__(self) -> utils.meta_prog.generics.cls_wrapper_data.GenericClassWrapperDataMixin.TAlias_generic_cls:
        return self.wrapped_generic_cls
