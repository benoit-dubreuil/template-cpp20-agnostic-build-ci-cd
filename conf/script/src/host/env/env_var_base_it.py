__all__ = ['EnvVarBaseIt']

from abc import ABCMeta, abstractmethod
from collections.abc import Iterator
from typing import Final, final

from .env_var import *
from .env_var_fwd import *


class EnvVarBaseIt(Iterator[T_Key], metaclass=ABCMeta):
    __has_itered_over_env: bool
    __env_var: Final[EnvVar]

    def __init__(self, env_var: EnvVar) -> None:
        self.__has_itered_over_env = False
        self.__env_var = env_var

    @final
    def get_env_var(self) -> EnvVar:
        return self.__env_var

    @final
    def __next__(self) -> T_Key:
        self.__verify_has_next()
        self.__has_itered_over_env = True

        return self.get_env_var().get_env_key()

    def __verify_has_next(self):
        if self.__has_itered_over_env:
            raise StopIteration()

    @abstractmethod
    def _peek_next(self) -> T_Key:
        raise NotImplementedError()
