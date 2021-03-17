from typing import Final


class CLIArg:
    DEFAULT_PREFIX: Final[str] = '-'

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
