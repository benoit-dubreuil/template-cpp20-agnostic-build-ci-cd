from typing import Final

from ..meta_prog.encapsulation import *
from ..meta_prog.introspection import *

__all__: TAlias_Macro_All = ['DEFAULT_PATH_ARG']

DEFAULT_PREFIX: Final[str] = '-'


@export
class CLIArg:

    def __init__(self, name: str, prefix: str = DEFAULT_PREFIX):
        super().__init__()

        self.__name = name
        self.prefix = prefix if prefix is not None else str()

    @property
    def name(self) -> str:
        if self.__name is None:
            self.__name = str()

        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__prefixed_name = self.prefix + name
        self.__name = name

    @property
    def prefixed_name(self) -> str:
        if self.__prefixed_name is None:
            self.__prefixed_name = str()

        return self.__prefixed_name

    @property
    def prefix(self) -> str:
        if self.prefixed_name.startswith(self.name):
            prefix = str()
        else:
            prefix = self.prefixed_name.removesuffix(self.name)

        return prefix

    @prefix.setter
    def prefix(self, prefix) -> None:
        self.__prefixed_name = prefix + self.name

    def __str__(self) -> str:
        return self.prefixed_name

    def __repr__(self) -> str:
        return f'{self.__class__.__name__} {{{self.__class__.prefix.fget.__name__}: {self.prefix}, {str(self.__class__.name.fget.__name__)}: {self.name}}}'


DEFAULT_PATH_ARG: Final[CLIArg] = CLIArg('path')
