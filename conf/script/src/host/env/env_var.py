import abc
import collections.abc
import os
import typing
from collections.abc import Iterator
from dataclasses import dataclass
from typing import Final, final

import host.env.env_var_fwd as _fwd
import utils.more_typing

_ENV_VAR_ITEM_COUNT: Final[int] = 1


@dataclass(init=False, order=True)
class EnvVar(collections.abc.Mapping[_fwd.T_Key, _fwd.T_Values]):
    __env_key: _fwd.T_Key
    __env_values: _fwd.T_Values

    def __init__(self, key_name=None, values=None) -> None:
        self.__env_key = key_name if key_name is not None else str()
        self.__env_values = values if values is not None else _fwd.T_Values()

    def get_env_key(self) -> _fwd.T_Key:
        return self.__env_key

    def get_env_values(self) -> _fwd.T_Values:
        return self.__env_values

    def iter_key(self) -> Iterator[_fwd.T_Key]:
        return EnvVarKeyIt(env_var=self)

    def iter_values(self) -> Iterator[_fwd.T_Values]:
        return iter(self.get_env_values())

    def __contains__(self, key: _fwd.T_Key) -> bool:
        self.__verify_key_type(key=key)
        env_key: _fwd.T_Key = self.get_env_key()

        return key is env_key or key == env_key

    def __getitem__(self, key: _fwd.T_Key) -> _fwd.T_Values:
        if key not in self:
            raise KeyError()

        return self.get_env_values()

    def __len__(self) -> int:
        return _ENV_VAR_ITEM_COUNT

    def __iter__(self) -> Iterator[_fwd.T_Key]:
        return self.iter_key()

    def __str__(self) -> str:
        assert self.__env_key is not None
        assert self.__env_values is not None

        joined_values = self.join_values()

        return f'{self.get_env_key()}={joined_values}'

    def join_values(self) -> str:
        return os.pathsep.join(self.get_env_values())

    @staticmethod
    def __verify_key_type(key: _fwd.T_Key) -> None:
        if not isinstance(key, typing.get_args(_fwd.T_Key)):
            raise TypeError()

    @staticmethod
    def __verify_single_value_type(single_value: _fwd.T_Single_Value) -> None:
        if not isinstance(single_value, typing.get_args(_fwd.T_Single_Value)):
            raise TypeError()

    @staticmethod
    def __verify_values_type(values: _fwd.T_Values) -> None:
        if not isinstance(values, typing.get_args(_fwd.T_Values)):
            raise TypeError()


class EnvVarSingleIt(Iterator[utils.more_typing.T_PathLike], metaclass=abc.ABCMeta):
    _has_itered_over_env: bool
    __env_var: Final[EnvVar]

    def __init__(self, env_var: EnvVar) -> None:
        self._has_itered_over_env = False
        self.__env_var = env_var

    @final
    def get_env_var(self) -> EnvVar:
        return self.__env_var

    @final
    def __next__(self) -> utils.more_typing.T_PathLike:
        self.__verify_has_next()
        self._has_itered_over_env = True

        return self.get_env_var().get_env_key()

    def __verify_has_next(self):
        if self._has_itered_over_env:
            raise StopIteration()

    @abc.abstractmethod
    def _peek_next(self) -> utils.more_typing.T_PathLike:
        raise NotImplementedError()


@final
class EnvVarKeyIt(_EnvVarSingleIt[_fwd.T_Key]):

    def _peek_next(self) -> _fwd.T_Key:
        return self.get_env_var().get_env_key()
