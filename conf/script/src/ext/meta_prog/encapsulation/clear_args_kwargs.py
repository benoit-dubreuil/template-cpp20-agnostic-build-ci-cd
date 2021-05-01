__all__ = ['ClearArgsKwargs']

from typing import Any


class ClearArgsKwargs:

    def __init__(self, *args, **kwargs) -> None:
        super().__init__()

    def __new__(cls, *args, **kwargs) -> Any:
        return super().__new__(cls)
