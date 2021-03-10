from pathlib import Path
from typing import NoReturn, Optional, Union

from build_system.compiler.compiler import Compiler
from build_system.compiler.host.get_info.location import msvc
import build_system.compiler.host.get_info.location.msvc.installation_path
from build_system.compiler.host.get_info.cli import cli_fetch_compiler_info, format_error_msg


def error_compiler_not_found() -> NoReturn:
    error_msg = format_error_msg(f'{Compiler.MSVC.name} compiler matching the requirements not found')
    raise FileNotFoundError(error_msg)


def _cli_no_arg_find_msvc_installation_path(compiler_installation_path: Optional[Path] = None) -> Union[Path, NoReturn]:
    compiler_installation_path: Optional[Path] = msvc.installation_path.find(compiler_installation_path)

    if compiler_installation_path is None:
        error_compiler_not_found()

    return compiler_installation_path


def cli_find_msvc_installation_path() -> None:
    cli_fetch_compiler_info(Compiler.MSVC, _cli_no_arg_find_msvc_installation_path, desc_compiler_info='location', help_path_meaning='installation')
