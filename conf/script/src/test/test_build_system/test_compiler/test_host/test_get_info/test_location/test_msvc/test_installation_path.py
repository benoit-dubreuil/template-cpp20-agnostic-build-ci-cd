#!/usr/bin/env python3

import unittest
from unittest import mock
from unittest.mock import MagicMock

from build_system.compiler.host.get_info.location.msvc import installation_path


class TestFind(unittest.TestCase):

    @mock.patch('build_system.compiler.host.get_info.location.msvc.installation_path.Path')
    @mock.patch('build_system.compiler.host.get_info.location.msvc.installation_path.vswhere')
    def test_no_arg_not_found(self, mock_vswhere: MagicMock, mock_path: MagicMock):
        mock_vswhere.find_first.return_value = None
        result = installation_path.find()

        mock_vswhere.find_first.assert_called_once_with(latest=True, prerelease=True, products=installation_path._ALL_PRODUCTS, prop=installation_path._PROP_INSTALLATION_PATH,
                                                        requires=installation_path._DEFAULT_REQUIRES)
        self.assertIsNone(result)
