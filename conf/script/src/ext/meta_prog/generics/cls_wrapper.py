from ..encapsulation import *
from .cls_wrapper_data import *


# TODO : functools -> wraps ?
@export
class GenericClassWrapperMixin(GenericClassWrapperDataMixin):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @property
    def __class__(self) -> TAlias_generic_cls:
        return self.wrapped_generic_cls
