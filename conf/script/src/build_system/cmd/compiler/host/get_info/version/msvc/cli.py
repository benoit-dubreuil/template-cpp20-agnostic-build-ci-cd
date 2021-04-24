__all__ = ['cli_fetch_msvc_version']

from pathlib import Path
from typing import NoReturn, Optional, Union

from ...cli import *
from build_system.compiler import *
from ext.error import *
from .impl import *


def _fetch_version_no_arg(compiler_installation_path: Optional[Path] = None) -> Union[CompilerVersion, NoReturn]:
    compiler_version: Optional[CompilerVersion] = fetch_msvc_version(compiler_installation_path)

    if compiler_version is None:
        raise CompilerNotFoundError()

    return compiler_version


def cli_fetch_msvc_version() -> None:
    fetch_compiler_info(compiler_family=CompilerFamily.MSVC,
                        fetch_compiler_info_func=_fetch_version_no_arg,
                        help_path_meaning='installation')
