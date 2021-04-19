from .data import *

from utils.meta_prog.encapsulation import *


@export
class GenericClassMixin(GenericsDataMixin):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def has_generics(self) -> bool:
        return len(self.generics_by_type_vars) > 0
