#!/usr/bin/env python3

import abc
import unittest

import utils.cli.main
from utils.error.meta import ErrorMeta


class TestErrorMeta(unittest.TestCase):

    def test_impl_extends_abc_exception(self):
        class ErrorMetaImpl(abc.ABC, Exception, metaclass=ErrorMeta):
            ...

        ErrorMetaImpl()


if utils.cli.main.is_caller_main():
    unittest.main()
