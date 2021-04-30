#!/usr/bin/env python3

__all__ = ['EnvVarTestParamDataComponents']

from os import pathsep
from pathlib import PurePath
from typing import Any, Final, final


@final
class EnvVarTestParamDataComponents:
    TAlias_param_types = Final[list[type]]
    TAlias_param_data_by_type = Final[dict[type: list[Any]]]
    TAlias_param_data_str = Final[list[str]]
    TAlias_param_data_path = Final[list[PurePath]]

    valid_key_data_str: TAlias_param_data_str = ['', 'key', 'test', '123', 'KEY', 'key_', '_key', 'z-abc', 'space space']
    valid_values_windows_path_data_str: TAlias_param_data_str = [
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
    valid_values_unix_path_data_str: TAlias_param_data_str = [
        '/usr',
        '/usr/',
        '/usr/tmp',
        '/usr/tmp/',
        '~']
    valid_values_data_str: TAlias_param_data_str = \
        valid_key_data_str + \
        [f'%{key_str}%' for key_str in valid_key_data_str] + \
        valid_values_windows_path_data_str + \
        valid_values_unix_path_data_str + \
        ['val1;',
         'val1;val2',
         'val1;val2;',
         'many_postfix_sep;;;;',
         ';;;;;many_prefix_sep']
    valid_values_data_path: TAlias_param_data_path = \
        [PurePath(values_path_str) for values_path_str in valid_values_windows_path_data_str] + \
        [PurePath(values_path_str) for values_path_str in valid_values_unix_path_data_str]
    valid_joined_values_data_str: TAlias_param_data_str = [
        pathsep.join(valid_key_data_str),
        pathsep.join(valid_values_windows_path_data_str),
        pathsep.join(valid_values_unix_path_data_str)]
