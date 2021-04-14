from utils.meta_prog.generics.cls_wrapper_data import GenericClassWrapperData


class GenericClassWrapper(GenericClassWrapperData):

    @property
    def __class__(self) -> GenericClassWrapperData.TAlias_generic_cls:
        return self.wrapped_generic_cls
