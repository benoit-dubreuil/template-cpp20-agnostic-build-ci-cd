from utils.meta_prog.generics.cls_mixin import GenericClassMixin


class GenericAwareClassProxy(GenericClassMixin):
    wrapped_generic_cls: type[GenericClassMixin]

    def __init__(self, wrapped_generic_cls: type[GenericClassMixin], *args, **kwargs) -> None:
        self.wrapped_generic_cls = wrapped_generic_cls
        super().__init__(*args, **kwargs)

    def __call__(self):
        return self.wrapped_generic_cls(generics=self.generics)
