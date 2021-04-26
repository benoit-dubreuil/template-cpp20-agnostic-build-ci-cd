__all__ = ['CLIArg']

from typing import Final


class CLIArg:
    _DEFAULT_PREFIX: Final[str] = '-'
    _DEFAULT_PATH_ARG_NAME: Final[str] = 'path'

    def __init__(self, name: str, prefix: str = _DEFAULT_PREFIX):
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

    @classmethod
    def create_default_path_arg(cls) -> 'CLIArg':
        return CLIArg(cls._DEFAULT_PATH_ARG_NAME)

    def __str__(self) -> str:
        return self.prefixed_name

    def __repr__(self) -> str:
        return f'{self.__class__.__name__} {{{self.__class__.prefix.fget.__name__}: {self.prefix}, {str(self.__class__.name.fget.__name__)}: {self.name}}}'
