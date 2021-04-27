__all__ = ['EnvVar']

import os
from collections.abc import Iterator
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Final, Generic, AnyStr, get_args

import host.env.env_var_fwd as _fwd


@dataclass(init=False, order=True)
class EnvVar(Mapping[_fwd.T_Key, list[_fwd.T_Single_Value]], Generic[_fwd.T_Key, _fwd.T_Single_Value]):
    __env_key: _fwd.T_Key
    __env_values: list[_fwd.T_Single_Value]

    __ENV_VAR_ITEM_COUNT: Final[int] = 1

    def __init__(self: _fwd.T_EnvVar,
                 key: _fwd.T_Key = None,
                 values: list[_fwd.T_Single_Value] = None) -> None:
        self.__env_key = key if key is not None else _fwd.T_Key()
        self.__env_values = values if values is not None else list[_fwd.T_Single_Value]

    @classmethod
    def create_from_joined_values(cls,
                                  key: _fwd.T_Key = None,
                                  joined_values: AnyStr = None) -> 'EnvVar':
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

    def cast_values_to_any_str(self, str_cls: type[AnyStr] = _fwd.TAlias_Default_AnyStr) -> list[AnyStr]:
        return [str_cls(value) for value in self.get_env_values()]

    def join_values(self, str_cls: type[AnyStr] = _fwd.TAlias_Default_AnyStr) -> AnyStr:
        casted_env_var_sep: AnyStr = str_cls(os.pathsep)
        casted_values: list[AnyStr] = self.cast_values_to_any_str(str_cls=str_cls)

        return casted_env_var_sep.join(casted_values)

    @classmethod
    def __verify_key_type(cls: type[_fwd.T_EnvVar], key: _fwd.T_Key) -> None:
        if not isinstance(key, get_args(cls)):
            raise TypeError()