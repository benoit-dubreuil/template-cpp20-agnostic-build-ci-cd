#!/usr/bin/env python3

__all__ = ['TestEnvVar']

import unittest

from ext.meta_prog.introspection import *
from host.env.env_var import *
from .env_var_test_param_data import *


class TestEnvVar(unittest.TestCase):

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

    def test_constructor_valid_generics_no_args_raises(self):
        with self.assertRaises(TypeError):
            _ = EnvVar[]()


if is_caller_main():
    unittest.main()
