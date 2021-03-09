#!/usr/bin/env python3

from typing import Final
from pathlib import Path

import vswhere
import colorama

import cli_fetch_compiler_version
from compiler_version import CompilerVersion
from data_model import Compiler

DEFAULT_REQUIRES: Final[list[str]] = [
    'Microsoft.VisualStudio.Component.VC.Tools.x86.x64',
    'Microsoft.VisualStudio.Component.Windows10SDK.19041',
    'Microsoft.VisualStudio.Component.VC.CMake.Project',
    'Microsoft.VisualStudio.Component.TestTools.BuildTools',
    'Microsoft.VisualStudio.Component.VC.ASAN',
    'Microsoft.VisualStudio.Component.VC.Modules.x86.x64',
    'Microsoft.VisualStudio.Workload.VCTools'
]

_ALL_PRODUCTS: Final[str] = '*'
_PROP_VERSION: Final[str] = 'installationVersion'
_PROP_INSTALLATION_PATH: Final[str] = 'installationPath'


def find_msvc_installation_path() -> Path or None:
    compiler_installation_path: Path or None = None
    found_compiler_version: str = vswhere.find_first(latest=True, prerelease=True, products=_ALL_PRODUCTS, prop=_PROP_INSTALLATION_PATH, requires=DEFAULT_REQUIRES)

    if found_compiler_version is not None:
        compiler_installation_path = Path(found_compiler_version.strip())

    return compiler_installation_path


def fetch_msvc_version() -> CompilerVersion or None:
    interpreted_compiler_version = None
    found_compiler_versions: list[str] = vswhere.find(latest=True, prerelease=True, products=_ALL_PRODUCTS, prop=_PROP_VERSION, requires=DEFAULT_REQUIRES)

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
    cli_fetch_compiler_version.cli_init()
    compiler_version: CompilerVersion = fetch_msvc_version()

    if compiler_version is not None:
        _print_found_compiler(compiler_version)
    else:
        _error_compiler_not_found()
