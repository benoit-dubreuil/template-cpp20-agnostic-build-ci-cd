#!/usr/bin/env python3

__all__ = ['TestEnvVar']

import unittest
from pathlib import Path
from os import PathLike

from host.env.env_var import *
from ext.meta_prog.introspection import *


class TestEnvVar(unittest.TestCase):
    __valid_key_generic_types = [str, bytes]
    __valid_values_generic_types = [str, bytes, Path]

    __invalid_key_generic_types = [type(None), int, bool, float]
    __invalid_values_generic_types = [type(None), int, bool, float]

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
