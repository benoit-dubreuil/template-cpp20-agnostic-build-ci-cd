from pathlib import Path
from typing import NoReturn, Optional, Union

from cli_fetch_compiler_info import cli_fetch_compiler_info
from version import CompilerVersion
from data_model import Compiler
from fetch_msvc_version import fetch_msvc_version
from cli_find_msvc_location import error_compiler_not_found


def _cli_no_arg_fetch_msvc_version(compiler_installation_path: Optional[Path] = None) -> Union[CompilerVersion, NoReturn]:
    compiler_version: Optional[CompilerVersion] = fetch_msvc_version(compiler_installation_path)

    if compiler_version is None:
        error_compiler_not_found()

    return compiler_version


def cli_fetch_msvc_version() -> None:
    cli_fetch_compiler_info(Compiler.MSVC, _cli_no_arg_fetch_msvc_version, help_path_meaning='installation')
