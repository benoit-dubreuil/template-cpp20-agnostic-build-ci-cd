#!/usr/bin/env python3

__all__ = ['TestEnvVar']

import unittest
from typing import Callable, Optional

from ext.meta_prog.introspection.caller import *
from host.env.env_var import *
from .env_var_test_param_data import EnvVarTestParamData as test_data
from collections import Iterable


class TestEnvVar(unittest.TestCase):

    def test_ref_cls_valid_generic_types(self):
        def _test_impl(key_type: type, values_type: type):
            _ = EnvVar[key_type, values_type]

        self.__with_valid_generic_types(test_func=_test_impl)

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

    def test_ref_cls_no_generics(self):
        _ = EnvVar

    @staticmethod
    def __for_generic_types(key_types: Iterable[type], values_types: Iterable[type], test_func: Callable[[type, type], None]):
        for key_type in key_types:
            for values_type in values_types:
                test_func(key_type, values_type)

    @classmethod
    def __for_valid_generic_types(cls, test_func: Callable[[type, type], None]):
        cls.__for_generic_types(key_types=test_data.valid_key_types,
                                values_types=test_data.valid_values_types,
                                test_func=test_func)

    def __with_valid_generic_types(self, test_func: Callable[[type, type], None], msg: Optional[str] = None):
        def wrap_subtest(key_type: type, values_type: type):
            kwargs = {'key_type': key_type,
                      'values_type': values_type}

            if msg is not None and len(msg) > 0:
                kwargs |= {'msg': msg}

            with self.subTest(**kwargs):
                test_func(key_type, values_type)

        self.__for_valid_generic_types(wrap_subtest)

    # TODO
    # def test_constructor_valid_generics_no_args_raises(self):
    #     with self.assertRaises(TypeError):
    #         _ = EnvVar[]()


if is_caller_main():
    unittest.main()
