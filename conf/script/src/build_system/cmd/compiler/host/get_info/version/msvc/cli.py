from pathlib import Path
from typing import NoReturn, Optional, Union

from build_system.compiler.family import CompilerFamily
from build_system.cmd.compiler.host.get_info import version
from build_system.cmd.compiler.host.get_info import cli
from build_system.compiler.version import CompilerVersion


def _fetch_version_no_arg(compiler_installation_path: Optional[Path] = None) -> Union[CompilerVersion, NoReturn]:
    compiler_version: Optional[CompilerVersion] = version.msvc.fetch(compiler_installation_path)

    if compiler_version is None:
        build_system.cmd.compiler.host.get_info.location.msvc.cli.error_compiler_not_found()

    return compiler_version


def fetch_version() -> None:
    cli.cli_fetch_compiler_info(CompilerFamily.MSVC, _fetch_version_no_arg, help_path_meaning='installation')
