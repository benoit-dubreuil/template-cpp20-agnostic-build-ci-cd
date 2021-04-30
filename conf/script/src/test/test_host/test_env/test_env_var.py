#!/usr/bin/env python3

__all__ = ['TestEnvVar']

import unittest
from typing import Callable, Optional

from ext.meta_prog.introspection import *
from host.env.env_var import *
from .env_var_test_param_data import EnvVarTestParamData as test_data
from ext.meta_prog.introspection.caller import *


class TestEnvVar(unittest.TestCase):

    def test_ref_cls_no_generics(self):
        _ = EnvVar

    @staticmethod
    def __for_valid_generic_types(test_func: Callable[[type, type], None]):
        for key_type in test_data.valid_key_types:
            for values_type in test_data.valid_values_data_by_type:
                test_func(key_type, values_type)

    def __with_valid_generic_types(self, test_func: Callable[[type, type], None], msg: Optional[str] = None):
        def wrap_subtest(key_type: type, values_type: type):
            with self.subTest(msg=msg, key_type=key_type, values_type=values_type):
                test_func(key_type, values_type)

        self.__for_valid_generic_types(wrap_subtest)

    def test_ref_cls_valid_generic_types(self):
        def _test_impl(key_type: type, values_type: type):
            _ = EnvVar[key_type, values_type]

        test_name: str = get_caller_func_name()
        self.__with_valid_generic_types(msg=test_name, test_func=_test_impl)

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

    def test_constructor_valid_generics_no_args_raises(self):
        with self.assertRaises(TypeError):
            _ = EnvVar[]()


if is_caller_main():
    unittest.main()
