#!/usr/bin/env python3

__all__ = ['TestEnvVar']

import unittest
from pathlib import Path
from os import PathLike

from host.env.env_var import *
from ext.meta_prog.introspection import *


class TestEnvVar(unittest.TestCase):

    def test_ref_cls_no_generics(self):
        _ = EnvVar

    def test_ref_cls_valid_generics(self):
        _ = EnvVar[str, str]


if is_caller_main():
    unittest.main()
