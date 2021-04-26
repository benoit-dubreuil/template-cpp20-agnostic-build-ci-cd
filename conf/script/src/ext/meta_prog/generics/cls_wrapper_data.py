__all__ = ['TAlias_generic_cls',
           'GenericClassWrapperDataMixin']

from typing import Final, Generic

TAlias_generic_cls = type[Generic]


class GenericClassWrapperDataMixin:
    wrapped_generic_cls: Final[TAlias_generic_cls]

    def __init__(self, generic_cls: TAlias_generic_cls, *args, **kwargs) -> None:
        self.wrapped_generic_cls = generic_cls
        super().__init__(*args, **kwargs)
