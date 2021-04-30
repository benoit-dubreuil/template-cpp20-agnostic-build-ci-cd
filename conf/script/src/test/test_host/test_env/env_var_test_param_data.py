#!/usr/bin/env python3

__all__ = ['EnvVarTestParamData']

from os import pathsep
from pathlib import PurePath
from typing import Any, Final, final

from ext.utils.string import *


@final
class EnvVarTestParamData:
    __TAlias_param_types = Final[list[type]]
    __TAlias_param_data_by_type = Final[dict[type: list[Any]]]
    __TAlias_param_data_str = Final[list[str]]
    __TAlias_param_data_path = Final[list[PurePath]]

    valid_key_types: __TAlias_param_types = [str, bytes]
    valid_values_types: __TAlias_param_types = [str, bytes, PurePath]
    valid_joined_values_types: __TAlias_param_types = [str, bytes]

    invalid_key_types: __TAlias_param_types = [type(None), int, bool, float]
    invalid_values_types: __TAlias_param_types = [type(None), int, bool, float]
    invalid_joined_values_types: __TAlias_param_types = [type(None), int, bool, float, PurePath]

    __valid_key_data_str: __TAlias_param_data_str = ['', 'key', 'test', '123', 'KEY', 'key_', '_key', 'z-abc', 'space space']
    __valid_values_windows_path_data_str: __TAlias_param_data_str = [
        'C:\\',
        'C:\\Users',
        'C:\\Users\\',
        'C:\\Users\\Public',
        'C:\\Users\\Public\\',
        'C:\\Users\\Public\\wow.doge',
        '.\\',
        '.\\Users',
        '.\\Users\\',
        '.\\Users\\Public',
        '.\\Users\\Public\\',
        '.\\Users\\Public\\wow.doge']
    __valid_values_unix_path_data_str: __TAlias_param_data_str = [
        '/usr',
        '/usr/',
        '/usr/tmp',
        '/usr/tmp/',
        '~']
    __valid_values_data_str: __TAlias_param_data_str = \
        __valid_key_data_str + \
        [f'%{key_str}%' for key_str in __valid_key_data_str] + \
        __valid_values_windows_path_data_str + \
        __valid_values_unix_path_data_str + \
        ['val1;',
         'val1;val2',
         'val1;val2;',
         'many_postfix_sep;;;;',
         ';;;;;many_prefix_sep']
    __valid_values_data_path: __TAlias_param_data_path = \
        [PurePath(values_path_str) for values_path_str in __valid_values_windows_path_data_str] + \
        [PurePath(values_path_str) for values_path_str in __valid_values_unix_path_data_str]
    __valid_joined_values_data_str: __TAlias_param_data_str = [
        pathsep.join(__valid_key_data_str),
        pathsep.join(__valid_values_windows_path_data_str),
        pathsep.join(__valid_values_unix_path_data_str)]

    __valid_key_data_by_type: __TAlias_param_data_by_type = {
        str: __valid_key_data_str,
        bytes: [key_str.encode(UTF_8) for key_str in __valid_key_data_str]
    }
    __valid_values_data_by_type: __TAlias_param_data_by_type = {
        str: __valid_values_data_str,
        bytes: [values_str.encode(UTF_8) for values_str in __valid_values_data_str],
        PurePath: __valid_values_data_path
    }
    __valid_joined_values_data_by_type: __TAlias_param_data_by_type = {
        str: __valid_joined_values_data_str,
        bytes: [values_str.encode(UTF_8) for values_str in __valid_joined_values_data_str],
    }

    # TODO
    invalid_key_data_by_type: __TAlias_param_data_by_type = {
        type(None): [None],
        int: [],
        bool: [],
        float: []
    }
    invalid_values_data_by_type: __TAlias_param_data_by_type = {
        type(None): [None],
        int: [],
        bool: [],
        float: []
    }
    invalid_joined_values_data_by_type: __TAlias_param_data_by_type = {
        type(None): [None],
        int: [],
        bool: [],
        float: [],
        PurePath: []
    }
