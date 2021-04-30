#!/usr/bin/env python3

__all__ = ['TestEnvVar']

import unittest
from pathlib import PurePath
from typing import Any, Final

from ext.meta_prog.introspection import *
from ext.utils.string import *
from host.env.env_var import *


class TestEnvVar(unittest.TestCase):
    __TAlias_param_types = Final[list[type]]
    __TAlias_param_data = Final[dict[type: list[Any]]]

    __valid_key_types: __TAlias_param_types = [str, bytes]
    __valid_values_types: __TAlias_param_types = [str, bytes, PurePath]

    __invalid_key_types: __TAlias_param_types = [type(None), int, bool, float]
    __invalid_values_types: __TAlias_param_types = [type(None), int, bool, float]

    __valid_key_data_str: Final[list[str]] = ['', 'key', 'test', '123', 'KEY', 'key_', '_key', 'z-abc', 'space space']
    __valid_values_path_data_str: Final[list[str]] = ['C:\\',
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
                                                      '.\\Users\\Public\\wow.doge',
                                                      '/usr',
                                                      '/usr/',
                                                      '/usr/tmp',
                                                      '/usr/tmp/',
                                                      '~']
    __valid_values_data_str: Final[list[str]] = __valid_key_data_str + \
                                                [f'%{key_str}%' for key_str in __valid_key_data_str] + \
                                                __valid_values_path_data_str + \
                                                ['val1;',
                                                 'val1;val2',
                                                 'val1;val2;',
                                                 'many_postfix_sep;;;;',
                                                 ';;;;;many_prefix_sep']
    __valid_values_data_path: Final[list[PurePath]] = [PurePath(values_path_str) for values_path_str in __valid_values_path_data_str]

    __valid_key_data_by_type: __TAlias_param_data = {
        str: __valid_key_data_str,
        bytes: [key_str.encode(UTF_8) for key_str in __valid_key_data_str]
    }

    __valid_values_data_by_type: __TAlias_param_data = {
        str: __valid_values_data_str,
        bytes: [values_str.encode(UTF_8) for values_str in __valid_values_data_str],
        PurePath: []
    }

    __invalid_key_data_by_type: __TAlias_param_data = {
        type(None): [],
        int: [],
        bool: [],
        float: []
    }

    __invalid_values_data_by_type: __TAlias_param_data = {
        type(None): [],
        int: [],
        bool: [],
        float: []
    }

    def test_ref_cls_no_generics(self):
        _ = EnvVar

    def test_ref_cls_valid_generics(self):
        _ = EnvVar[str, str]

    def test_constructor_no_generics_no_args_raises(self):
        with self.assertRaises(TypeError):
            _ = EnvVar()

    def test_constructor_no_generics_only_key_arg_raises(self):
        with self.assertRaises(TypeError):
            _ = EnvVar(key='key')

    def test_constructor_no_generics_only_values_arg_raises(self):
        with self.assertRaises(TypeError):
            _ = EnvVar(values=['values'])

    def test_constructor_no_generics_only_empty_values_arg_raises(self):
        with self.assertRaises(TypeError):
            _ = EnvVar(values=[])


if is_caller_main():
    unittest.main()
