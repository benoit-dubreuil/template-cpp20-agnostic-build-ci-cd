#!/usr/bin/env python3

__all__ = ['TestEnvVar']

import unittest
from collections import Iterable
from typing import Callable, Optional

from ext.meta_prog.introspection.caller import *
from host.env.env_var import *
from .env_var_test_param_data import EnvVarTestParamData as test_data


class TestEnvVar(unittest.TestCase):
    __TAlias_generic_test_func = Callable[[type, type], None]

    def test_ref_cls_no_generics(self):
        _ = EnvVar
        self.assertIs(_, EnvVar)

    def test_ref_cls_valid_generic_types(self):
        def _test_impl(key_type: type, values_type: type):
            _ = EnvVar[key_type, values_type]

        self.__with_valid_generic_types(test_func=_test_impl)

    # TODO : See TODO in `ext.meta_prog.generics.proxy_verifier_mixin.ProxyGenericsVerifierMixin._verify_generics`
    @unittest.skip('Skipping due to missing feature : verify if a type respects a TypeVar\'s constraints.')
    def test_ref_cls_invalid_generic_types(self):
        def _test_impl(key_type: type, values_type: type):
            with self.assertRaises(TypeError):
                _ = EnvVar[key_type, values_type]

        self.__with_invalid_generic_types(test_func=_test_impl)

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

    @staticmethod
    def __for_generic_types(key_types: Iterable[type],
                            values_types: Iterable[type],
                            test_func: __TAlias_generic_test_func):
        for key_type in key_types:
            for values_type in values_types:
                test_func(key_type, values_type)

    @classmethod
    def __for_valid_generic_types(cls, test_func: __TAlias_generic_test_func):
        cls.__for_generic_types(key_types=test_data.valid_key_types,
                                values_types=test_data.valid_values_types,
                                test_func=test_func)

    @classmethod
    def __for_invalid_generic_types(cls, test_func: __TAlias_generic_test_func):
        cls.__for_generic_types(key_types=test_data.invalid_key_types,
                                values_types=test_data.invalid_values_types,
                                test_func=test_func)

    def __with_generic_types(self,
                             generic_types_iterative_func: type[__for_valid_generic_types],
                             test_func: __TAlias_generic_test_func,
                             msg: Optional[str] = None):
        def wrap_subtest(key_type: type, values_type: type):
            kwargs = {'key_type': key_type,
                      'values_type': values_type}

            if msg is not None and len(msg) > 0:
                kwargs |= {'msg': msg}

            with self.subTest(**kwargs):
                test_func(key_type, values_type)

        generic_types_iterative_func(test_func=wrap_subtest)

    def __with_valid_generic_types(self,
                                   test_func: __TAlias_generic_test_func,
                                   msg: Optional[str] = None):
        self.__with_generic_types(generic_types_iterative_func=self.__for_valid_generic_types,
                                  test_func=test_func,
                                  msg=msg)

    def __with_invalid_generic_types(self,
                                     test_func: __TAlias_generic_test_func,
                                     msg: Optional[str] = None):
        self.__with_generic_types(generic_types_iterative_func=self.__for_invalid_generic_types,
                                  test_func=test_func,
                                  msg=msg)

    # TODO
    # def test_constructor_valid_generics_no_args_raises(self):
    #     with self.assertRaises(TypeError):
    #         _ = EnvVar[]()


if is_caller_main():
    unittest.main()
