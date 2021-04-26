__all__ = ['TAlias_Generics_By_TypeVars',
           'GenericsDataMixin']

from typing import Final, Optional, TypeVar

TAlias_Generics_By_TypeVars = dict[TypeVar, Optional[type]]


class GenericsDataMixin:
    generics_by_type_vars: Final[TAlias_Generics_By_TypeVars]

    def __init__(self, *args,
                 generics_by_type_vars: TAlias_Generics_By_TypeVars = None,
                 **kwargs) -> None:
        self.generics_by_type_vars = generics_by_type_vars if generics_by_type_vars is not None else {}
        super().__init__(*args, **kwargs)
