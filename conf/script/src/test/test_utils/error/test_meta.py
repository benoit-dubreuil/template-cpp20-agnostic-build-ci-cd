#!/usr/bin/env python3

import abc
import unittest

import utils.cli.main
from utils.error.meta import ErrorMeta


class TestErrorMeta(unittest.TestCase):

    def test_impl_extends_exception(self):
        class ErrorMetaImpl(Exception, metaclass=ErrorMeta):
            ...

        ErrorMetaImpl()

    def test_impl_extends_exception_abstractmethod(self):
        class ErrorMetaImplParent(Exception, metaclass=ErrorMeta):

            @abc.abstractmethod
            def dummy(self):
                ...

        class ErrorMetaImplChild(ErrorMetaImplParent, metaclass=ErrorMeta):

            def dummy(self):
                ...

        ErrorMetaImplChild()


if utils.cli.main.is_caller_main():
    unittest.main()
