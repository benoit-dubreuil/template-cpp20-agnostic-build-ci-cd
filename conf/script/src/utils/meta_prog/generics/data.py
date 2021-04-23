import typing


__all__ = ['TAlias_Generics_By_TypeVars']

TAlias_Generics_By_TypeVars = dict[TypeVar, Optional[type]]


@export
class GenericsDataMixin:
    TAlias_Generics_By_TypeVars = dict[typing.TypeVar, typing.Optional[type]]

    generics_by_type_vars: typing.Final[TAlias_Generics_By_TypeVars]

    def __init__(self, *args,
                 generics_by_type_vars: TAlias_Generics_By_TypeVars = None,
                 **kwargs) -> None:
        self.generics_by_type_vars = generics_by_type_vars if generics_by_type_vars is not None else {}
        super().__init__(*args, **kwargs)
