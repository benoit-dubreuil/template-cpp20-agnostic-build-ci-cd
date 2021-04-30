#!/usr/bin/env python3

__all__ = ['TestEnvVar']

import unittest
from pathlib import Path
from os import PathLike
from typing import Final, Any

from host.env.env_var import *
from ext.meta_prog.introspection import *


class TestEnvVar(unittest.TestCase):
    __valid_key_types: Final[list[type]] = [str, bytes]
    __valid_values_types: Final[list[type]] = [str, bytes, Path]

    __invalid_key_types: Final[list[type]] = [type(None), int, bool, float]
    __invalid_values_types: Final[list[type]] = [type(None), int, bool, float]

    __valid_key_data_by_type: Final[dict[type: list[Any]]] = {
        str: [],
        bytes: []
    }

    __valid_values_data_by_type: Final[dict[type: list[Any]]] = {
        str: [],
        bytes: [],
        Path: []
    }

    __invalid_key_data_by_type: Final[dict[type: list[Any]]] = {
        type(None): [],
        int: [],
        bool: [],
        float: []
    }

    __invalid_values_data_by_type: Final[dict[type: list[Any]]] = {
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
