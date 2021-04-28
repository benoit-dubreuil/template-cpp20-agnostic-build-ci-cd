#!/usr/bin/env python3

__all__ = ['TestEnvVar']

import unittest
from typing import Final
from unittest import mock
from unittest.mock import MagicMock

import host.env.env_var
from ext.meta_prog.introspection import *


class TestEnvVar(unittest.TestCase):
    ...


if is_caller_main():
    unittest.main()
