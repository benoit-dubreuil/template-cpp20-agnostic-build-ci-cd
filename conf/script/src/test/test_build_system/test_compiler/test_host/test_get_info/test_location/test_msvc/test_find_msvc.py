#!/usr/bin/env python3

import unittest
from unittest import mock
from unittest.mock import MagicMock

import build_system.cmd.compiler.host.get_info.location.msvc
from ext.meta_prog.introspection import *


class TestFindMSVC(unittest.TestCase):

    @mock.patch('build_system.cmd.compiler.host.get_info.location.msvc.impl.vswhere')
    def test_no_arg_not_found(self, mock_vswhere: MagicMock):
        mock_vswhere.find_first.return_value = None
        result = build_system.cmd.compiler.host.get_info.location.msvc.find_location()

        mock_vswhere.find_first.assert_called_once_with(latest=True, prerelease=True,
                                                        products=build_system.cmd.compiler.host.get_info.location.msvc.impl._ALL_PRODUCTS,
                                                        prop=build_system.cmd.compiler.host.get_info.location.msvc.impl._PROP_INSTALLATION_PATH,
                                                        requires=build_system.cmd.compiler.host.get_info.location.msvc.impl._DEFAULT_REQUIRES)
        self.assertIsNone(result)


if is_caller_main():
    unittest.main()
