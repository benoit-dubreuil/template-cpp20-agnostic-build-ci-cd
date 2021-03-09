from typing import NoReturn

import colorama

from compiler_version import CompilerVersion
from data_model import Compiler
from fetch_msvc_version import fetch_msvc_version


def _print_found_compiler(compiler_version: CompilerVersion) -> None:
    print(compiler_version, end=str())


def _error_compiler_not_found() -> NoReturn:
    error_msg = colorama.Style.BRIGHT + colorama.Fore.RED
    error_msg += f'{Compiler.MSVC.name} compiler matching the requirements not found'
    error_msg += colorama.Style.RESET_ALL

    raise FileNotFoundError(error_msg)


def cli_fetch_msvc_version() -> None:
    compiler_version: CompilerVersion = fetch_msvc_version()

    if compiler_version is not None:
        _print_found_compiler(compiler_version)
    else:
        _error_compiler_not_found()
