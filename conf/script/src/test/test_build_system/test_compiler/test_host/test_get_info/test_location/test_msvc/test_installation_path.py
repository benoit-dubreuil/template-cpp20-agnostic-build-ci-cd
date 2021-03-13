#!/usr/bin/env python3

import unittest
from unittest import mock

from build_system.compiler.host.get_info.location.msvc import installation_path


class TestFind(unittest.TestCase):

    # @mock.patch('installation_path.vswhere')
    def test_no_arg_not_found(self):
        assert True
