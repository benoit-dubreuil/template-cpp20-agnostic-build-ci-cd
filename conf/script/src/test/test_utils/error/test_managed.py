#!/usr/bin/env python3

import unittest

import utils.error.core.format
import utils.error.core.managed
import utils.error.core.meta
import utils.error.core.status
from utils.meta_prog.introspection import *


class TestManage(unittest.TestCase):

    def assert_decorated_error_type(self, decorated_error_cls: type):
        self.assertEqual(type(decorated_error_cls), utils.error.core.meta.ErrorMeta)
        self.assertIsInstance(decorated_error_cls(), utils.error.core.managed.ManagedErrorMixin)
        self.assertNotIsInstance(decorated_error_cls(), utils.error.core.managed.ManageClass)

    def test_decorate_error(self):
        @utils.error.core.managed.ManageClass(encoded_error_status=utils.error.core.status.ErrorStatus.UNSUPPORTED)
        class DecoratedError(RuntimeError):

            def __init__(self):
                super().__init__(str(unittest))

        self.assert_decorated_error_type(DecoratedError)

    def test_raise_decorated_error(self):
        @utils.error.core.managed.ManageClass(encoded_error_status=utils.error.core.status.ErrorStatus.UNSUPPORTED)
        class DecoratedError(RuntimeError):

            def __init__(self):
                super().__init__(str(unittest))

        with self.assertRaises(DecoratedError):
            raise DecoratedError()

    def test_overriden_error_status_of_raised_decorated_error(self):
        @utils.error.core.managed.ManageClass()
        class DecoratedError(RuntimeError):

            def __init__(self):
                super().__init__(str(unittest))

            @staticmethod
            def get_error_status() -> utils.error.core.status.ErrorStatus:
                return utils.error.core.status.ErrorStatus.UNSUPPORTED

        with self.assertRaises(DecoratedError) as context_manager:
            raise DecoratedError()

        raised_error = context_manager.exception
        self.assertEqual(utils.error.core.status.ErrorStatus.UNSUPPORTED, raised_error.get_error_status())

    def test_param_error_status_of_raised_decorated_error(self):
        @utils.error.core.managed.ManageClass(encoded_error_status=utils.error.core.status.ErrorStatus.UNSUPPORTED)
        class DecoratedError(RuntimeError):

            def __init__(self):
                super().__init__(str(unittest))

        with self.assertRaises(DecoratedError) as context_manager:
            raise DecoratedError()

        raised_error = context_manager.exception
        self.assertEqual(utils.error.core.status.ErrorStatus.UNSUPPORTED, raised_error.get_error_status())

    def test_overriden_param_error_status_of_raised_decorated_error(self):
        @utils.error.core.managed.ManageClass(encoded_error_status=utils.error.core.status.ErrorStatus.SUCCESS)
        class DecoratedError(RuntimeError):

            def __init__(self):
                super().__init__(str(unittest))

            @staticmethod
            def get_error_status() -> utils.error.core.status.ErrorStatus:
                return utils.error.core.status.ErrorStatus.UNSUPPORTED

        with self.assertRaises(DecoratedError) as context_manager:
            raise DecoratedError()

        raised_error = context_manager.exception
        self.assertEqual(utils.error.core.status.ErrorStatus.UNSUPPORTED, raised_error.get_error_status())

    def test_decorate_warning(self):
        @utils.error.core.managed.ManageClass(encoded_error_status=utils.error.core.status.ErrorStatus.UNSUPPORTED)
        class DecoratedError(RuntimeWarning):

            def __init__(self):
                super().__init__(str(unittest))

        DecoratedError()
        self.assert_decorated_error_type(DecoratedError)

    def test_decorate_success_with_formatter(self):
        @utils.error.core.managed.ManageClass(error_formatter_cls=utils.error.core.format.FormattedSuccessMixin, encoded_error_status=utils.error.core.status.ErrorStatus.SUCCESS)
        class DecoratedError(UserWarning):

            def __init__(self):
                super().__init__(str(unittest))

        DecoratedError()
        self.assert_decorated_error_type(DecoratedError)

    def test_decorate_success_with_formatter_and_overriden_status(self):
        @utils.error.core.managed.ManageClass(error_formatter_cls=utils.error.core.format.FormattedSuccessMixin)
        class DecoratedError(UserWarning):

            def __init__(self):
                super().__init__(str(unittest))

            @staticmethod
            def get_error_status() -> utils.error.core.status.ErrorStatus:
                return utils.error.core.status.ErrorStatus.SUCCESS

        DecoratedError()
        self.assert_decorated_error_type(DecoratedError)

    def test_decorate_success_with_formatter_and_status(self):
        @utils.error.core.managed.ManageClass(error_formatter_cls=utils.error.core.format.FormattedSuccessMixin, encoded_error_status=utils.error.core.status.ErrorStatus.SUCCESS)
        class DecoratedError(UserWarning):

            def __init__(self):
                super().__init__(str(unittest))

        DecoratedError()
        self.assert_decorated_error_type(DecoratedError)


if is_caller_main():
    unittest.main()
