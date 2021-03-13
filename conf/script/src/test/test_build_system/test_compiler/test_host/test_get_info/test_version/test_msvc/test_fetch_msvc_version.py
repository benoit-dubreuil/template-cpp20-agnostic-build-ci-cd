#!/usr/bin/env python3

import unittest
from unittest import mock
from unittest.mock import MagicMock

from build_system.compiler.host.get_info.version.msvc import fetch_msvc_version


class TestFetch(unittest.TestCase):

    @mock.patch('build_system.compiler.host.get_info.version.msvc.fetch_msvc_version.vswhere')
    @mock.patch('build_system.compiler.host.get_info.version.msvc.fetch_msvc_version.msvc.installation_path')
    def test_no_arg_return_none(self, mock_installation_path: MagicMock, mock_vswhere: MagicMock):
        mock_installation_path.find.return_value = None

        result = fetch_msvc_version.fetch()

        mock_installation_path.find.assert_called_once_with(None)

        assert len(mock_installation_path.mock_calls) == 1
        assert len(mock_vswhere.mock_calls) == 0

        self.assertIsNone(result)
