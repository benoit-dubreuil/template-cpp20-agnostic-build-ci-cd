__all__ = ['GenericClassProxy']

import itertools
from typing import Any, TypeVar

from .cls_wrapper import *
from .cls_wrapper_data import *
from .data import *
from ..encapsulation import *
from .proxy_verifier_mixin import *


# TODO : functools -> wraps ?
class GenericClassProxy(ProxyGenericsVerifierMixin,
                        GenericsDataMixin,
                        GenericClassWrapperMixin,
                        ClearArgsKwargs):

    def __new__(cls,
                generic_cls: TAlias_generic_cls,
                *args,
                generics: tuple[type] = tuple(),
                **kwargs):
        generics_by_type_vars = cls.__create_generics_by_type_vars(generic_cls=generic_cls, generics=generics)
        return super().__new__(cls, *args, generic_cls=generic_cls, generics_by_type_vars=generics_by_type_vars, **kwargs)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        return self.wrapped_generic_cls(*args, generics_by_type_vars=self.generics_by_type_vars, **kwargs)

    def __getattribute__(self, name: str) -> Any:
        attr: Any

        try:
            attr = super().__getattribute__(name)
        except AttributeError:
            attr = getattr(self.wrapped_generic_cls, name)

        return attr

    @classmethod
    def __create_generics_by_type_vars(cls,
                                       generic_cls: TAlias_generic_cls,
                                       generics: tuple[type]) \
            -> TAlias_Generics_By_TypeVars:
        type_vars = cls.__detect_type_vars(generic_cls=generic_cls)
        generics_by_type_vars = dict(itertools.zip_longest(type_vars, generics, fillvalue=None))

        return generics_by_type_vars

    @classmethod
    def __detect_type_vars(cls,
                           generic_cls: TAlias_generic_cls) \
            -> list[TypeVar]:
        from typing import TypeVar, Generic, get_args, get_origin

        type_vars: list[TypeVar] = []

        for orig_base in generic_cls.__orig_bases__:
            if get_origin(orig_base) is Generic:
                base_type_args = get_args(orig_base)

                if len(base_type_args) > 0:
                    for type_arg in base_type_args:
                        if isinstance(type_arg, TypeVar):
                            type_vars.append(type_arg)
                else:
                    type_vars += cls.__detect_type_vars(generic_cls=orig_base)

        return type_vars
