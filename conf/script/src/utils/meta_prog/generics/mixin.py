from utils.meta_prog.generics.data import GenericsData


class GenericClassMixin(GenericsData):
    from typing import Final, TypeVar

    type_vars: Final[tuple[TypeVar]]

    def __init__(self, *args, type_vars: tuple[TypeVar] = tuple(), **kwargs):
        self.type_vars = type_vars
        super().__init__(*args, **kwargs)

    def has_generics(self) -> bool:
        return len(self.generics) > 0
