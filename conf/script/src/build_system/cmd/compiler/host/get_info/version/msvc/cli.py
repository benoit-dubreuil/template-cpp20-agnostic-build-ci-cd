from pathlib import Path
from typing import NoReturn, Optional, Union

import build_system.cmd.compiler.host.get_info.cli
import build_system.cmd.compiler.host.get_info.location.msvc.cli
import build_system.compiler.core.family
import build_system.compiler.core.version
import ext.error.core.cls_def


def _fetch_version_no_arg(compiler_installation_path: Optional[Path] = None) -> Union[build_system.compiler.core.version.CompilerVersion, NoReturn]:
    compiler_version: Optional[build_system.compiler.core.version.CompilerVersion] = build_system.cmd.compiler.host.get_info.version.msvc.fetch_version(compiler_installation_path)

    if compiler_version is None:
        raise ext.error.core.cls_def.CompilerNotFoundError()

    return compiler_version


def fetch_version() -> None:
    build_system.cmd.compiler.host.get_info.cli.fetch_compiler_info(compiler_family=build_system.compiler.core.family.CompilerFamily.MSVC,
                                                                    fetch_compiler_info_func=_fetch_version_no_arg,
                                                                    help_path_meaning='installation')
