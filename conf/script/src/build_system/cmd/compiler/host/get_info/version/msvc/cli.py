from pathlib import Path
from typing import NoReturn, Optional, Union

import build_system.cmd.compiler.host.get_info.cli
import build_system.cmd.compiler.host.get_info.location.msvc.cli
import build_system.compiler.family
import build_system.compiler.version


def _fetch_version_no_arg(compiler_installation_path: Optional[Path] = None) -> Union[build_system.compiler.version.CompilerVersion, NoReturn]:
    compiler_version: Optional[build_system.compiler.version.CompilerVersion] = build_system.cmd.compiler.host.get_info.version.msvc.fetch(compiler_installation_path)

    if compiler_version is None:
        build_system.cmd.compiler.host.get_info.location.msvc.cli.error_compiler_not_found()

    return compiler_version


def fetch_version() -> None:
    build_system.cmd.compiler.host.get_info.cli.cli_fetch_compiler_info(build_system.compiler.family.CompilerFamily.MSVC, _fetch_version_no_arg, help_path_meaning='installation')
