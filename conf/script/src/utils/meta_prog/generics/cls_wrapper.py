from utils.meta_prog.generics.cls_wrapper_data import GenericClassWrapperDataMixin


class GenericClassWrapperMixin(GenericClassWrapperDataMixin):

    @property
    def __class__(self) -> GenericClassWrapperDataMixin.TAlias_generic_cls:
        return self.wrapped_generic_cls
