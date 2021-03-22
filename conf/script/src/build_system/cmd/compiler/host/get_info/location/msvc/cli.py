from pathlib import Path
from typing import NoReturn, Optional, Union

import build_system.cmd.compiler.host.get_info.cli
import build_system.compiler.family
import utils.error.cls_def


def _find_no_arg(compiler_installation_path: Optional[Path] = None) -> Union[Path, NoReturn]:
    compiler_installation_path: Optional[Path] = build_system.cmd.compiler.host.get_info.location.msvc.find_location(compiler_installation_path)

    if compiler_installation_path is None:
        raise utils.error.cls_def.CompilerNotFoundError()

    return compiler_installation_path


def find() -> None:
    build_system.cmd.compiler.host.get_info.cli.fetch_compiler_info(build_system.compiler.family.CompilerFamily.MSVC,
                                                                    _find_no_arg, desc_compiler_info='location',
                                                                    help_path_meaning='installation')
