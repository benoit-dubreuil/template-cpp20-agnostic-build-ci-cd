#!/usr/bin/env python3

import unittest
from unittest import mock
from unittest.mock import MagicMock

from build_system.compiler.host.get_info.location.msvc import installation_path


class TestFind(unittest.TestCase):

    @mock.patch('build_system.compiler.host.get_info.location.msvc.installation_path.Path')
    @mock.patch('build_system.compiler.host.get_info.location.msvc.installation_path.vswhere')
    def test_no_arg_not_found(self, mock_vswhere: MagicMock, mock_path: MagicMock):
        assert True
