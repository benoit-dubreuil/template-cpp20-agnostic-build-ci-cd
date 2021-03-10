from pathlib import Path
from typing import NoReturn, Optional, Union

from build_system.compiler.compiler import Compiler
from build_system.compiler.version import CompilerVersion

from build_system.compiler.host.get_info.cli import cli_fetch_compiler_info

from build_system.compiler.host.get_info.location import msvc
import build_system.compiler.host.get_info.location.msvc.cli

from build_system.compiler.host.get_info.version import msvc
import build_system.compiler.host.get_info.version.msvc.fetch_msvc_version


def _cli_no_arg_fetch_msvc_version(compiler_installation_path: Optional[Path] = None) -> Union[CompilerVersion, NoReturn]:
    compiler_version: Optional[CompilerVersion] = msvc.fetch_msvc_version.fetch_msvc_version(compiler_installation_path)

    if compiler_version is None:
        msvc.cli.error_compiler_not_found()

    return compiler_version


def cli_fetch_msvc_version() -> None:
    cli_fetch_compiler_info(Compiler.MSVC, _cli_no_arg_fetch_msvc_version, help_path_meaning='installation')
