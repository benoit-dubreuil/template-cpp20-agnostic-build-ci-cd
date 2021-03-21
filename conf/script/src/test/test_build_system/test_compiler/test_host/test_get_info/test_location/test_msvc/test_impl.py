#!/usr/bin/env python3

import unittest
from unittest import mock
from unittest.mock import MagicMock

import build_system.cmd.compiler.host.get_info.location.msvc
import utils.cli.main


class TestFind(unittest.TestCase):

    @mock.patch('build_system.compiler.host.get_info.location.msvc.installation_path.vswhere')
    def test_no_arg_not_found(self, mock_vswhere: MagicMock):
        mock_vswhere.find_first.return_value = None
        result = build_system.cmd.compiler.host.get_info.location.msvc.find()

        mock_vswhere.find_first.assert_called_once_with(latest=True, prerelease=True,
                                                        products=build_system.cmd.compiler.host.get_info.location.msvc.impl._ALL_PRODUCTS,
                                                        prop=build_system.cmd.compiler.host.get_info.location.msvc.impl._PROP_INSTALLATION_PATH,
                                                        requires=build_system.cmd.compiler.host.get_info.location.msvc.impl._DEFAULT_REQUIRES)
        self.assertIsNone(result)


if utils.cli.main.is_caller_main():
    unittest.main()
