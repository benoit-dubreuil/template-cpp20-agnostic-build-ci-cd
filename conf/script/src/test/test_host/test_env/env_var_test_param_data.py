#!/usr/bin/env python3

__all__ = ['EnvVarTestParamData']

from pathlib import PurePath
from typing import final

from ext.utils.string import *
from ._env_var_test_param_data_components import EnvVarTestParamDataComponents as _fwd


@final
class EnvVarTestParamData:
    valid_key_types: _fwd.TAlias_param_types = [str, bytes]
    valid_values_types: _fwd.TAlias_param_types = [str, bytes, PurePath]
    valid_joined_values_types: _fwd.TAlias_param_types = [str, bytes]

    invalid_key_types: _fwd.TAlias_param_types = [type(None), int, bool, float]
    invalid_values_types: _fwd.TAlias_param_types = [type(None), int, bool, float]
    invalid_joined_values_types: _fwd.TAlias_param_types = [type(None), int, bool, float, PurePath]

    valid_key_data_by_type: _fwd.TAlias_param_data_by_type = {
        str: _fwd.valid_key_data_str,
        bytes: [_key_str.encode(UTF_8) for _key_str in _fwd.valid_key_data_str]
    }
    valid_values_data_by_type: _fwd.TAlias_param_data_by_type = {
        str: _fwd.valid_values_data_str,
        bytes: [_values_str.encode(UTF_8) for _values_str in _fwd.valid_values_data_str],
        PurePath: _fwd.valid_values_data_path
    }
    valid_joined_values_data_by_type: _fwd.TAlias_param_data_by_type = {
        str: _fwd.valid_joined_values_data_str,
        bytes: [_values_str.encode(UTF_8) for _values_str in _fwd.valid_joined_values_data_str],
    }

    invalid_key_data_by_type: _fwd.TAlias_param_data_by_type = {
        type(None): _fwd.invalid_param_data_none,
        int: _fwd.invalid_param_data_int,
        bool: _fwd.invalid_param_data_bool,
        float: _fwd.invalid_param_data_float
    }
    invalid_values_data_by_type: _fwd.TAlias_param_data_by_type = {
        type(None): _fwd.invalid_param_data_none,
        int: _fwd.invalid_param_data_int,
        bool: _fwd.invalid_param_data_bool,
        float: _fwd.invalid_param_data_float
    }
    invalid_joined_values_data_by_type: _fwd.TAlias_param_data_by_type = {
        type(None): _fwd.invalid_param_data_none,
        int: _fwd.invalid_param_data_int,
        bool: _fwd.invalid_param_data_bool,
        float: _fwd.invalid_param_data_float,
        PurePath: _fwd.invalid_joined_values_data_path
    }
