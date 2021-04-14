import dataclasses
import typing

from utils.meta_prog.generics.mixin import GenericClassMixin


@dataclasses.dataclass()
class GenericClassWrapperData:
    TAlias_generic_cls = type[GenericClassMixin, typing.Generic]

    wrapped_generic_cls: typing.Final[TAlias_generic_cls]

    def __init__(self, generic_cls: TAlias_generic_cls, *args, **kwargs) -> None:
        self.wrapped_generic_cls = generic_cls
        super().__init__(*args, **kwargs)
