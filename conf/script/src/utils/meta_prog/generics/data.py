import dataclasses
import typing


@dataclasses.dataclass()
class GenericsData:
    generics: typing.Final[tuple[type]]

    def __init__(self, *args, generics: tuple[type] = tuple(), **kwargs) -> None:
        self.generics = generics
        super().__init__(*args, **kwargs)
