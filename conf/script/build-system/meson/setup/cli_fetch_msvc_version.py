from pathlib import Path
from typing import NoReturn, Optional, Union

import colorama

from cli_fetch_compiler_version import cli_fetch_compiler_version
from compiler_version import CompilerVersion
from data_model import Compiler
from fetch_msvc_version_impl import fetch_msvc_version


def _error_compiler_not_found() -> NoReturn:
    error_msg = colorama.Style.BRIGHT + colorama.Fore.RED
    error_msg += f'{Compiler.MSVC.name} compiler matching the requirements not found'
    error_msg += colorama.Style.RESET_ALL

    raise FileNotFoundError(error_msg)


def _cli_no_arg_fetch_msvc_version(compiler_installation_path: Optional[Path] = None) -> Union[CompilerVersion, NoReturn]:
    compiler_version: Optional[CompilerVersion] = fetch_msvc_version(compiler_installation_path)

    if compiler_version is None:
        _error_compiler_not_found()

    return compiler_version


def cli_fetch_msvc_version() -> None:
    cli_fetch_compiler_version(Compiler.MSVC, _cli_no_arg_fetch_msvc_version, help_path_meaning='installation')
