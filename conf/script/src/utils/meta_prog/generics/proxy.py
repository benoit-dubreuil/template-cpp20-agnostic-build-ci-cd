from utils.meta_prog.generics.mixin import GenericClassMixin


class GenericClassProxy(GenericClassMixin):
    from typing import TypeVar, Generic

    _TAlias_generic_cls = type[GenericClassMixin, Generic]

    wrapped_generic_cls: _TAlias_generic_cls

    def __init__(self, generic_cls: _TAlias_generic_cls, *args, **kwargs) -> None:
        self.wrapped_generic_cls = generic_cls
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        return self.wrapped_generic_cls(*args, generics=self.generics, **kwargs)

    @property
    def __class__(self) -> _TAlias_generic_cls:
        return self.wrapped_generic_cls
