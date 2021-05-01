__all__ = ['TAlias_generic_cls',
           'GenericClassWrapperDataMixin']

from typing import Generic

TAlias_generic_cls = type[Generic]


class GenericClassWrapperDataMixin:
    wrapped_generic_cls: TAlias_generic_cls

    def __new__(cls, generic_cls: TAlias_generic_cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        instance.wrapped_generic_cls = generic_cls

        return instance

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
