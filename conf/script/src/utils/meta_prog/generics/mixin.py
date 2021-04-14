class GenericClassMixin:
    from typing import Final, TypeVar

    generics: Final[tuple[type]]
    type_vars: Final[tuple[TypeVar]]

    def __init__(self, *args, type_vars: tuple[TypeVar] = None, generics: tuple[type] = None, **kwargs):
        self.generics = generics if generics is not None else tuple()
        self.type_vars = type_vars if type_vars is not None else tuple()

        super().__init__(*args, **kwargs)

    def has_generics(self) -> bool:
        return len(self.generics) > 0
