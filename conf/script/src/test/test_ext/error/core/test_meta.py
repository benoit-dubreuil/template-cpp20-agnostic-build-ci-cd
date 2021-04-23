#!/usr/bin/env python3

import abc
import unittest

from ext.error import *
from ext.meta_prog.introspection import *


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
                raise NotImplementedError()

        class ErrorMetaImplChild(ErrorMetaImplParent, metaclass=ErrorMeta):

            def dummy(self):
                ...

        ErrorMetaImplChild()


if is_caller_main():
    unittest.main()
