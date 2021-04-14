import collections.abc
import os
import typing
from collections.abc import Iterator
from dataclasses import dataclass
from typing import Final

import host.env.env_var_fwd as _fwd


@dataclass(init=False, order=True)
class EnvVar(collections.abc.Mapping[_fwd.T_Key, _fwd.T_Values]):
    __env_key: _fwd.T_Key
    __env_values: _fwd.T_Values

    __ENV_VAR_ITEM_COUNT: Final[int] = 1

    def __init__(self, key: _fwd.T_Key = None, values: _fwd.T_Values = None) -> None:
        self.__env_key = key if key is not None else _fwd.T_Key()
        self.__env_values = values if values is not None else _fwd.T_Values()

    def get_env_key(self) -> _fwd.T_Key:
        return self.__env_key

    def get_env_values(self) -> _fwd.T_Values:
        return self.__env_values

    def iter_key(self) -> Iterator[_fwd.T_Key]:
        from host.env.env_var_key_it import EnvVarKeyIt
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
        return self.__ENV_VAR_ITEM_COUNT

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
