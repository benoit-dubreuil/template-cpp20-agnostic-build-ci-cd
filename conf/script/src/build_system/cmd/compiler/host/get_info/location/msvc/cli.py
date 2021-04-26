__all__ = ['cli_find_msvc_location']

from pathlib import Path
from typing import NoReturn, Optional, Union

from ...cli import *
from .impl import *
from build_system.compiler import *
from ext.error import *


def _find_no_arg(compiler_installation_path: Optional[Path] = None) -> Union[Path, NoReturn]:
    compiler_installation_path: Optional[Path] = find_msvc_location(compiler_installation_path)

    if compiler_installation_path is None:
        raise CompilerNotFoundError()

    return compiler_installation_path


def cli_find_msvc_location() -> None:
    fetch_compiler_info(CompilerFamily.MSVC,
                        _find_no_arg, desc_compiler_info='location',
                        help_path_meaning='installation')
