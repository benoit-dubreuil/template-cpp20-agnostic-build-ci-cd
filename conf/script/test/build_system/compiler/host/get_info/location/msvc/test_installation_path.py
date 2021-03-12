#!/usr/bin/env python3
from build_system.compiler.host.get_info.location.msvc import installation_path

import unittest
from unittest import mock
from unittest.mock import MagicMock


class Find(unittest.TestCase):

    @mock.patch('installation_path.Path')
    @mock.patch('installation_path.vswhere')
    def test_no_arg_not_found(self, mock_vswhere: MagicMock, mock_path: MagicMock):
        mock_vswhere.find_first.return_value = None
        result = installation_path.find()
        self.assertIsNone(result)
