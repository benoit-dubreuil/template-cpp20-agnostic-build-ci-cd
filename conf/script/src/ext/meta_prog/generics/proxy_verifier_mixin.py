__all__ = ['ProxyGenericsVerifierMixin']

from .data import *
from .cls_wrapper_data import *
from typing import Tuple, TypeVar, Generic


class ProxyGenericsVerifierMixin(GenericsDataMixin, GenericClassWrapperDataMixin):

    def __new__(cls, *args, **kwargs):
        instance: cls = super().__new__(cls, *args, **kwargs)
        instance._verify_generics()

        return instance

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def _verify_generics(self) -> None:
        generic_type_vars: tuple[TypeVar] = self.__get_cls_generic_type_vars(self.wrapped_generic_cls)

        if len(self.generics_by_type_vars) != len(generic_type_vars):
            raise TypeError(f'Wrong number of generic types for {type(self.wrapped_generic_cls)}.')

        if tuple(self.generics_by_type_vars.keys()) != generic_type_vars:
            raise TypeError(f'Supplied generic types do not match the class\'s generic type vars requirements.')

    @staticmethod
    def __get_cls_generic_type_vars(cls: TAlias_generic_cls) -> tuple[TypeVar]:
        return cls.__parameters__
