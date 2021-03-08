#!/usr/bin/env python3

from typing import Final

import vswhere
import colorama

import fetch_compiler_version
from compiler_version import CompilerVersion
from data_model import Compiler

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


def find_msvc_compiler_version() -> CompilerVersion or None:
    interpreted_compiler_version = None
    found_compiler_versions: list[str] = vswhere.find(latest=True, prerelease=True, products=DEFAULT_ALL_PRODUCTS, prop=DEFAULT_PROP_VERSION, requires=DEFAULT_REQUIRES)

    if len(found_compiler_versions) > 0:
        first_compiler_version: str = found_compiler_versions[0].strip()
        interpreted_compiler_version = CompilerVersion.create_from_str(first_compiler_version)

    return interpreted_compiler_version


def _print_found_compiler(compiler_version: CompilerVersion):
    print(compiler_version, end=str())


def _error_compiler_not_found():
    error_msg = colorama.Style.BRIGHT + colorama.Fore.RED
    error_msg += f'{Compiler.MSVC.name} compiler matching the requirements not found'
    error_msg += colorama.Style.RESET_ALL

    raise FileNotFoundError(error_msg)


# Run as a script
if __name__ == '__main__':
    fetch_compiler_version.cli_init()
    compiler_version: CompilerVersion = find_msvc_compiler_version()

    if compiler_version is not None:
        _print_found_compiler(compiler_version)
    else:
        _error_compiler_not_found()
