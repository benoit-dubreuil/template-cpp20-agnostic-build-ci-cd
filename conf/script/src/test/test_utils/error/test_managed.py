#!/usr/bin/env python3

import unittest

import utils.cli.main
import utils.error.format
import utils.error.status
from utils.error.managed import manage


class TestManage(unittest.TestCase):

    def test_decorate_success_with_formatter_and_status(self):
        @manage(error_formatter_cls=utils.error.format.FormattedSuccess, encoded_error_status=utils.error.status.ErrorStatus.SUCCESS)
        class SuccessWarning(UserWarning):

            def __init__(self):
                super().__init__('Success')

        SuccessWarning()


if utils.cli.main.is_caller_main():
    unittest.main()
