import typing

import utils.meta_prog.generics.cls_mixin


class GenericClassWrapperDataMixin:
    TAlias_generic_cls = type[utils.meta_prog.generics.cls_mixin.GenericClassMixin, typing.Generic]

    wrapped_generic_cls: typing.Final[TAlias_generic_cls]

    def __init__(self, generic_cls: TAlias_generic_cls, *args, **kwargs) -> None:
        self.wrapped_generic_cls = generic_cls
        super().__init__(*args, **kwargs)
