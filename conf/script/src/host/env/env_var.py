__all__ = ['EnvVar']

import os
from collections.abc import Iterator
from collections.abc import Mapping
from dataclasses import dataclass
from typing import AnyStr, Final, Generic, get_args

from ext.meta_prog.generics import *
from .env_var_fwd import *


@dataclass(init=False, order=True)
class EnvVar(GenericClassProxyInjectorMixin, Mapping[T_Env_Key, TAlias_Env_Values], Generic[T_Env_Key, T_Env_Single_Val]):
    __env_key: T_Env_Key
    __env_values: TAlias_Env_Values

    __ENV_VAR_ITEM_COUNT: Final[int] = 1

    def __init__(self: T_EnvVar,
                 *args,
                 key: T_Env_Key = None,
                 values: TAlias_Env_Values = None,
                 **kwargs) -> None:
        super().__init__(*args, **kwargs)

        generic_env_key: type = self.generics_by_type_vars[T_Env_Key]

        self.__env_key = key if key is not None else generic_env_key()
        self.__env_values = values if values is not None else TAlias_Env_Values()

    @classmethod
    def create_from_joined_values(cls,
                                  key: T_Env_Key = None,
                                  joined_values: AnyStr = None) -> 'EnvVar':
        # TODO
        ...

    @classmethod
    def __split_joined_values(cls, joined_values: AnyStr) -> list[AnyStr]:
        env_values_sep: AnyStr = cls.__get_env_values_sep(joined_values_cls=type(joined_values))
        split_values: list[AnyStr] = joined_values.split(sep=env_values_sep)

        return split_values

    @classmethod
    def __cast_split_values(cls, split_values: list[AnyStr]) -> TAlias_Env_Values:
        generic_env_single_val: type = cls.generics_by_type_vars[T_Env_Single_Val]
        return [generic_env_single_val(value) for value in split_values]

    def get_env_key(self) -> T_Env_Key:
        return self.__env_key

    def get_env_values(self) -> TAlias_Env_Values:
        return self.__env_values

    def iter_key(self) -> Iterator[T_Env_Key]:
        from host.env.env_var_key_it import EnvVarKeyIt
        return EnvVarKeyIt(env_var=self)

    def iter_values(self) -> Iterator[T_Env_Single_Val]:
        return iter(self.get_env_values())

    def __contains__(self, key: T_Env_Key) -> bool:
        self.__verify_key_type(key=key)
        env_key: T_Env_Key = self.get_env_key()

        return key is env_key or key == env_key

    def __getitem__(self, key: T_Env_Key) -> TAlias_Env_Values:
        if key not in self:
            raise KeyError()

        return self.get_env_values()

    def __len__(self) -> int:
        return self.__ENV_VAR_ITEM_COUNT

    def __iter__(self) -> Iterator[T_Env_Key]:
        return self.iter_key()

    def __str__(self) -> str:
        assert self.__env_key is not None
        assert self.__env_values is not None

        joined_values = self.join_values()

        return f'{self.get_env_key()}={joined_values}'

    @staticmethod
    def __get_env_values_sep(joined_values_cls: type[AnyStr]) -> AnyStr:
        return joined_values_cls(os.pathsep)

    def cast_values_to_any_str(self, str_cls: type[AnyStr] = AnyStr) -> list[AnyStr]:
        return [str_cls(value) for value in self.get_env_values()]

    def join_values(self, str_cls: type[AnyStr] = AnyStr) -> AnyStr:
        casted_env_var_sep: AnyStr = str_cls(os.pathsep)
        casted_values: list[AnyStr] = self.cast_values_to_any_str(str_cls=str_cls)

        return casted_env_var_sep.join(casted_values)

    @classmethod
    def __verify_key_type(cls: type[T_EnvVar], key: T_Env_Key) -> None:
        if not isinstance(key, get_args(cls)):
            raise TypeError()
