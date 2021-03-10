from pathlib import Path
from typing import NoReturn, Optional, Union

from cli_fetch_compiler_info import cli_fetch_compiler_info, format_error_msg
from data_model import Compiler
from find_msvc_location_impl import find_msvc_installation_path


def error_compiler_not_found() -> NoReturn:
    error_msg = format_error_msg(f'{Compiler.MSVC.name} compiler matching the requirements not found')
    raise FileNotFoundError(error_msg)


def _cli_no_arg_fetch_msvc_location(compiler_installation_path: Optional[Path] = None) -> Union[Path, NoReturn]:
    compiler_installation_path: Optional[Path] = find_msvc_installation_path(compiler_installation_path)

    if compiler_installation_path is None:
        error_compiler_not_found()

    return compiler_installation_path


def cli_find_msvc_location() -> None:
    cli_fetch_compiler_info(Compiler.MSVC, _cli_no_arg_fetch_msvc_location, desc_compiler_info='location', help_path_meaning='installation')
