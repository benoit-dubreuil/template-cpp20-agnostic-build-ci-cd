#!/usr/bin/env python3

import unittest

from ext.error import *
from ext.meta_prog.introspection import *


class TestManage(unittest.TestCase):

    def assert_decorated_error_type(self, decorated_error_cls: type):
        self.assertEqual(type(decorated_error_cls), ErrorMeta)
        self.assertIsInstance(decorated_error_cls(), ManagedErrorMixin)
        self.assertNotIsInstance(decorated_error_cls(), ManageClass)

    def test_decorate_error(self):
        @ManageClass(encoded_error_status=ErrorStatus.UNSUPPORTED)
        class DecoratedError(RuntimeError):

            def __init__(self):
                super().__init__(str(unittest))

        self.assert_decorated_error_type(DecoratedError)

    def test_raise_decorated_error(self):
        @ManageClass(encoded_error_status=ErrorStatus.UNSUPPORTED)
        class DecoratedError(RuntimeError):

            def __init__(self):
                super().__init__(str(unittest))

        with self.assertRaises(DecoratedError):
            raise DecoratedError()

    def test_overriden_error_status_of_raised_decorated_error(self):
        @ManageClass()
        class DecoratedError(RuntimeError):

            def __init__(self):
                super().__init__(str(unittest))

            @staticmethod
            def get_error_status() -> ErrorStatus:
                return ErrorStatus.UNSUPPORTED

        with self.assertRaises(DecoratedError) as context_manager:
            raise DecoratedError()

        raised_error = context_manager.exception
        self.assertEqual(ErrorStatus.UNSUPPORTED, raised_error.get_error_status())

    def test_param_error_status_of_raised_decorated_error(self):
        @ManageClass(encoded_error_status=ErrorStatus.UNSUPPORTED)
        class DecoratedError(RuntimeError):

            def __init__(self):
                super().__init__(str(unittest))

        with self.assertRaises(DecoratedError) as context_manager:
            raise DecoratedError()

        raised_error = context_manager.exception
        self.assertEqual(ErrorStatus.UNSUPPORTED, raised_error.get_error_status())

    def test_overriden_param_error_status_of_raised_decorated_error(self):
        @ManageClass(encoded_error_status=ErrorStatus.SUCCESS)
        class DecoratedError(RuntimeError):

            def __init__(self):
                super().__init__(str(unittest))

            @staticmethod
            def get_error_status() -> ErrorStatus:
                return ErrorStatus.UNSUPPORTED

        with self.assertRaises(DecoratedError) as context_manager:
            raise DecoratedError()

        raised_error = context_manager.exception
        self.assertEqual(ErrorStatus.UNSUPPORTED, raised_error.get_error_status())

    def test_decorate_warning(self):
        @ManageClass(encoded_error_status=ErrorStatus.UNSUPPORTED)
        class DecoratedError(RuntimeWarning):

            def __init__(self):
                super().__init__(str(unittest))

        DecoratedError()
        self.assert_decorated_error_type(DecoratedError)

    def test_decorate_success_with_formatter(self):
        @ManageClass(error_formatter_cls=FormattedSuccessMixin, encoded_error_status=ErrorStatus.SUCCESS)
        class DecoratedError(UserWarning):

            def __init__(self):
                super().__init__(str(unittest))

        DecoratedError()
        self.assert_decorated_error_type(DecoratedError)

    def test_decorate_success_with_formatter_and_overriden_status(self):
        @ManageClass(error_formatter_cls=FormattedSuccessMixin)
        class DecoratedError(UserWarning):

            def __init__(self):
                super().__init__(str(unittest))

            @staticmethod
            def get_error_status() -> ErrorStatus:
                return ErrorStatus.SUCCESS

        DecoratedError()
        self.assert_decorated_error_type(DecoratedError)

    def test_decorate_success_with_formatter_and_status(self):
        @ManageClass(error_formatter_cls=FormattedSuccessMixin, encoded_error_status=ErrorStatus.SUCCESS)
        class DecoratedError(UserWarning):

            def __init__(self):
                super().__init__(str(unittest))

        DecoratedError()
        self.assert_decorated_error_type(DecoratedError)


if is_caller_main():
    unittest.main()
