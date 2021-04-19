#!/usr/bin/env python3

import abc
import unittest

import utils.error.core.meta
from utils.meta_prog.introspection import *


class TestErrorMeta(unittest.TestCase):

    def test_is_instance(self):
        self.assertIsInstance(utils.error.core.meta.ErrorMeta, type)
        self.assertNotIsInstance(utils.error.core.meta.ErrorMeta, abc.ABCMeta)

    def test_impl_is_instance(self):
        class ErrorMetaImpl(metaclass=utils.error.core.meta.ErrorMeta):
            ...

        self.assertIsInstance(ErrorMetaImpl, type)
        self.assertIsInstance(ErrorMetaImpl, abc.ABCMeta)
        self.assertIsInstance(ErrorMetaImpl(), ErrorMetaImpl)

    def test_impl_extends_exception(self):
        class ErrorMetaImpl(Exception, metaclass=utils.error.core.meta.ErrorMeta):
            ...

        ErrorMetaImpl()

    def test_impl_extends_exception_abstractmethod(self):
        class ErrorMetaImplParent(Exception, metaclass=utils.error.core.meta.ErrorMeta):

            @abc.abstractmethod
            def dummy(self):
                raise NotImplementedError()

        class ErrorMetaImplChild(ErrorMetaImplParent, metaclass=utils.error.core.meta.ErrorMeta):

            def dummy(self):
                ...

        ErrorMetaImplChild()


if is_caller_main():
    unittest.main()
