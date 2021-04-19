from typing import Final, Optional, TypeVar

from utils.meta_prog.encapsulation import *


@export
class GenericsDataMixin:
    TAlias_Generics_By_TypeVars = dict[TypeVar, Optional[type]]

    generics_by_type_vars: Final[TAlias_Generics_By_TypeVars]

    def __init__(self, *args,
                 generics_by_type_vars: TAlias_Generics_By_TypeVars = None,
                 **kwargs) -> None:
        self.generics_by_type_vars = generics_by_type_vars if generics_by_type_vars is not None else {}
        super().__init__(*args, **kwargs)
