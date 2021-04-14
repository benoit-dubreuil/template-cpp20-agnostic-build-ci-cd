import abc
import collections.abc

import host.env.env_var
import host.env.env_var_fwd as _fwd


class EnvVarBaseIt(collections.abc.Iterator[_fwd.T_Key], metaclass=abc.ABCMeta):
    from host.env.env_var import EnvVar
    from typing import Final, final

    __has_itered_over_env: bool
    __env_var: Final[host.env.env_var.EnvVar]

    def __init__(self, env_var: EnvVar) -> None:
        self.__has_itered_over_env = False
        self.__env_var = env_var

    @final
    def get_env_var(self) -> EnvVar:
        return self.__env_var

    @final
    def __next__(self) -> _fwd.T_Key:
        self.__verify_has_next()
        self.__has_itered_over_env = True

        return self.get_env_var().get_env_key()

    def __verify_has_next(self):
        if self.__has_itered_over_env:
            raise StopIteration()

    @abc.abstractmethod
    def _peek_next(self) -> _fwd.T_Key:
        raise NotImplementedError()
