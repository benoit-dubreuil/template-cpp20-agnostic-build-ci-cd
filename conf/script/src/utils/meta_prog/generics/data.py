import dataclasses
import typing


@dataclasses.dataclass()
class GenericsData:
    generics_by_type_vars: typing.Final[dict[typing.TypeVar, type]]

    def __init__(self, *args,
                 generics_by_type_vars: dict[typing.TypeVar, type] = None,
                 **kwargs) -> None:
        self.generics_by_type_vars = generics_by_type_vars if generics_by_type_vars is not None else {}
        super().__init__(*args, **kwargs)
