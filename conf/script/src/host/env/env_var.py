import collections.abc
import os
import typing
from collections.abc import Iterator
from dataclasses import dataclass
from typing import Final

import host.env.env_var_fwd as _fwd


@dataclass(init=False, order=True)
class EnvVar(typing.Generic[_fwd.T_Key, _fwd.T_Single_Value], collections.abc.Mapping[_fwd.T_Key, list[_fwd.T_Single_Value]]):
    __env_key: _fwd.T_Key
    __env_values: list[_fwd.T_Single_Value]

    __ENV_VAR_ITEM_COUNT: Final[int] = 1

    def __init__(self,
                 key: _fwd.T_Key = None,
                 values: list[_fwd.T_Single_Value] = None) -> None:
        self.__env_key = key if key is not None else _fwd.T_Key()
        self.__env_values = values if values is not None else list[_fwd.T_Single_Value]

    @classmethod
    def create_from_joined_values(cls,
                                  key: _fwd.T_Key = None,
                                  joined_values: typing.AnyStr = None) -> 'EnvVar':
        # TODO
        ...

    def get_env_key(self) -> _fwd.T_Key:
        return self.__env_key

    def get_env_values(self) -> list[_fwd.T_Single_Value]:
        return self.__env_values

    def iter_key(self) -> Iterator[_fwd.T_Key]:
        from host.env.env_var_key_it import EnvVarKeyIt
        return EnvVarKeyIt(env_var=self)

    def iter_values(self) -> Iterator[_fwd.T_Single_Value]:
        return iter(self.get_env_values())

    def __contains__(self, key: _fwd.T_Key) -> bool:
        self.__verify_key_type(key=key)
        env_key: _fwd.T_Key = self.get_env_key()

        return key is env_key or key == env_key

    def __getitem__(self, key: _fwd.T_Key) -> list[_fwd.T_Single_Value]:
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

    def cast_values_to_any_str(self, str_cls: type[typing.AnyStr] = _fwd.TAlias_Default_AnyStr) -> list[typing.AnyStr]:
        return [str_cls(value) for value in self.get_env_values()]

    def join_values(self, str_cls: type[typing.AnyStr] = _fwd.TAlias_Default_AnyStr) -> typing.AnyStr:
        casted_env_var_sep: typing.AnyStr = str_cls(os.pathsep)
        casted_values: list[typing.AnyStr] = self.cast_values_to_any_str(str_cls=str_cls)

        return casted_env_var_sep.join(casted_values)

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
