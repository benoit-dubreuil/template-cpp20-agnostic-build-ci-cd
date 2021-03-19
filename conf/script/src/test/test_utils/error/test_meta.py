#!/usr/bin/env python3

import abc
import unittest

import utils.cli.main
from utils.error.meta import ErrorMeta


class TestErrorMeta(unittest.TestCase):

    def test_is_instance(self):
        self.assertIsInstance(ErrorMeta, type)
        self.assertNotIsInstance(ErrorMeta, abc.ABCMeta)

    def test_impl_is_instance(self):
        class ErrorMetaImpl(metaclass=ErrorMeta):
            ...

        self.assertIsInstance(ErrorMetaImpl, type)
        self.assertIsInstance(ErrorMetaImpl, abc.ABCMeta)
        self.assertIsInstance(ErrorMetaImpl(), ErrorMetaImpl)

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
