#!/usr/bin/env python3

from typing import Final

import vswhere
import sys
import colorama

from compiler_version import CompilerVersion

DEFAULT_ALL_PRODUCTS: Final[str] = '*'
DEFAULT_PROP_VERSION: Final[str] = 'installationVersion'
DEFAULT_REQUIRES: Final[list[str]] = [
    'Microsoft.VisualStudio.Component.VC.Tools.x86.x64',
    'Microsoft.VisualStudio.Component.Windows10SDK.19041',
    'Microsoft.VisualStudio.Component.VC.CMake.Project',
    'Microsoft.VisualStudio.Component.TestTools.BuildTools',
    'Microsoft.VisualStudio.Component.VC.ASAN',
    'Microsoft.VisualStudio.Component.VC.Modules.x86.x64',
    'Microsoft.VisualStudio.Workload.VCTools'
]


def _print_found_compiler(found_msvc: list[str]):
    compiler_version_str: str = found_msvc[0].strip()
    compiler_version: CompilerVersion = CompilerVersion.create_from_str(compiler_version_str)
    print(compiler_version, end=str())


def _print_error_compiler_not_found():
    print(colorama.Style.BRIGHT + colorama.Fore.RED, file=sys.stderr, end=str())
    print('No MSVC compiler matching the requirements found', end=str())
    print(colorama.Style.RESET_ALL, file=sys.stderr, end=str())


# Run as a script
if __name__ == '__main__':
    colorama.init()
    found_msvc: list[str] = vswhere.find(latest=True, prerelease=True, products=DEFAULT_ALL_PRODUCTS, prop=DEFAULT_PROP_VERSION, requires=DEFAULT_REQUIRES)

    if len(found_msvc) > 0:
        _print_found_compiler(found_msvc)
    else:
        _print_error_compiler_not_found()
