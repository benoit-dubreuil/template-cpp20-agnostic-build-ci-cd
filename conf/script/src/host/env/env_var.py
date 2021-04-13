import collections.abc
import os
import typing
from dataclasses import dataclass
from typing import Iterator

from utils.more_typing import PathLike

_T_Key = PathLike
_T_Single_Val = PathLike
_T_Multi_Val = list[_T_Single_Val]


@dataclass(init=False, order=True)
class EnvVar(collections.abc.Mapping[_T_Key, _T_Multi_Val]):
    __env_key: _T_Key
    __env_values: _T_Multi_Val

    def __init__(self, key_name=None, values=None) -> None:
        self.values()
        self.__env_key = key_name if key_name is not None else str()
        self.__env_values = values if values is not None else _T_Multi_Val()

    def __contains__(self, key: _T_Key) -> bool:
        self.__verify_key_type(key=key)
        return key is self.__env_key or key == self.__env_key

    def __getitem__(self, key: _T_Key) -> _T_Multi_Val:
        if key not in self:
            raise KeyError()

        return self.__env_values

    def __eq__(self, o: object) -> bool:
        # TODO
        return super().__eq__(o)

    def __len__(self) -> int:
        return 1

    def __iter__(self) -> Iterator[_T_Key]:
        # TODO
        ...

    def __str__(self) -> str:
        assert self.__env_key is not None
        assert self.__env_values is not None

        joined_values = self.join_values()

        return f'{self.__env_key}={joined_values}'

    def join_values(self) -> str:
        return os.pathsep.join(self.__env_values)

    @staticmethod
    def __verify_key_type(key: _T_Key) -> None:
        if not isinstance(key, typing.get_args(_T_Key)):
            raise TypeError()

    @staticmethod
    def __verify_single_value_type(single_value: _T_Single_Val) -> None:
        if not isinstance(single_value, typing.get_args(_T_Key)):
            raise TypeError()

    @staticmethod
    def __verify_multi_value_type(multi_value: _T_Multi_Val) -> None:
        if not isinstance(multi_value, typing.get_args(_T_Single_Val)):
            raise TypeError()
