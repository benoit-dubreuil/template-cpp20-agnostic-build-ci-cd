from pathlib import Path
from typing import NoReturn, Optional, Union

from build_system.compiler.family import CompilerFamily
from build_system.cmd.compiler.host.get_info import location
from build_system.cmd.compiler.host.get_info.cli import cli_fetch_compiler_info
from utils.error.format import format_error_msg


def error_compiler_not_found() -> NoReturn:
    error_msg = format_error_msg(f'{CompilerFamily.MSVC.name} compiler matching the requirements not found')
    raise FileNotFoundError(error_msg)


def _find_no_arg(compiler_installation_path: Optional[Path] = None) -> Union[Path, NoReturn]:
    compiler_installation_path: Optional[Path] = location.msvc.find(compiler_installation_path)

    if compiler_installation_path is None:
        error_compiler_not_found()

    return compiler_installation_path


def find() -> None:
    cli_fetch_compiler_info(CompilerFamily.MSVC, _find_no_arg, desc_compiler_info='location', help_path_meaning='installation')
