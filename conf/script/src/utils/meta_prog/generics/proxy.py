from utils.meta_prog.generics.mixin import GenericClassMixin


class GenericClassProxy(GenericClassMixin):
    wrapped_generic_cls: type[GenericClassMixin]

    def __init__(self, generic_cls: type[GenericClassMixin], *args, **kwargs) -> None:
        self.wrapped_generic_cls = generic_cls
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        return self.wrapped_generic_cls(*args, generics=self.generics, **kwargs)

    @property
    def __class__(self) -> type[GenericClassMixin]:
        return self.wrapped_generic_cls
