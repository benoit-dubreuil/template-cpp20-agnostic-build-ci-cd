__all__ = ['EnvVar']

import os
from collections.abc import Iterator
from collections.abc import Mapping
from typing import AnyStr, Final, Generic, Optional

from ext.meta_prog.encapsulation import *
from ext.meta_prog.generics import *
from ext.utils.path import *
from ext.utils.string import *
from .env_var_fwd import *


class EnvVar(GenericClassProxyInjectorMixin, Mapping[T_Env_Key, TAlias_Env_Values], Generic[T_Env_Key, T_Env_Single_Val], ClearArgsKwargs):
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

        assert generic_env_key is not (type(None))
        assert self.generics_by_type_vars[T_Env_Single_Val] is not (type(None))

        self.__verify_key_type(key=key)

        self.__env_key = key if key is not None else generic_env_key()
        self.__env_values = values if values is not None else TAlias_Env_Values()

    @classmethod
    def create_from_joined_values(cls,
                                  key: T_Env_Key,
                                  joined_values: AnyStr) -> T_EnvVar:
        split_values: list[AnyStr] = cls.__split_joined_values(joined_values=joined_values)
        env_values: TAlias_Env_Values = cls.__cast_split_values(split_values=split_values)

        return cls(key=key, values=env_values)

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
        joined_values = self.join_values(str_cls=str)
        return f'{self.get_env_key()}={joined_values}'

    def get_env_key(self) -> T_Env_Key:
        return self.__env_key

    def get_env_values(self) -> TAlias_Env_Values:
        return self.__env_values

    def iter_key(self) -> Iterator[T_Env_Key]:
        from host.env.env_var_key_it import EnvVarKeyIt
        return EnvVarKeyIt(env_var=self)

    def iter_values(self) -> Iterator[T_Env_Single_Val]:
        return iter(self.get_env_values())

    def cast_values_to_any_str(self, target_cls: type[AnyStr]) -> list[AnyStr]:
        return [cast_any_str(target_cls=target_cls, src_any_str=value) for value in self.get_env_values()]

    def join_values(self, str_cls: type[AnyStr]) -> AnyStr:
        env_values_sep: AnyStr = self.__get_env_values_sep(joined_values_cls=str_cls)
        casted_values: list[AnyStr] = self.cast_values_to_any_str(target_cls=str_cls)

        return env_values_sep.join(casted_values)

    @staticmethod
    def __get_env_values_sep(joined_values_cls: type[AnyStr]) -> AnyStr:
        return cast_any_str(target_cls=joined_values_cls, src_any_str=os.pathsep)

    @classmethod
    def __split_joined_values(cls, joined_values: AnyStr) -> list[AnyStr]:
        split_values: list[AnyStr] = joined_values.strip(env_values_sep).split(sep=env_values_sep)

        return split_values

    @classmethod
    def __cast_split_values(cls, split_values: list[AnyStr]) -> TAlias_Env_Values:
        generic_env_single_val = cls.__get_type_env_single_val()
        return [cast_path_like(target_cls=generic_env_single_val, src_path_like=value) for value in split_values]

    @classmethod
    def __verify_key_type(cls: type[T_EnvVar], key: T_Env_Key) -> None:
        generic_env_key = cls.generics_by_type_vars[T_Env_Key]

        if not isinstance(key, generic_env_key):
            raise TypeError()

    @classmethod
    def __get_type_env_single_val(cls) -> type[T_Env_Single_Val]:
        type_env_single_val: Optional[type[T_Env_Single_Val]] = cls.generics_by_type_vars[T_Env_Single_Val]
        assert type_env_single_val is not (type(None))

        return cast(type[T_Env_Single_Val], type_env_single_val)
