__all__ = ['TAlias_Generics_By_TypeVars',
           'GenericsDataMixin']

from typing import Optional, TypeVar

TAlias_Generics_By_TypeVars = dict[TypeVar, Optional[type]]


class GenericsDataMixin:
    generics_by_type_vars: TAlias_Generics_By_TypeVars

    def __new__(cls,
                *args,
                generics_by_type_vars: TAlias_Generics_By_TypeVars = None,
                **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        instance.generics_by_type_vars = generics_by_type_vars if generics_by_type_vars is not None else {}

        return instance
