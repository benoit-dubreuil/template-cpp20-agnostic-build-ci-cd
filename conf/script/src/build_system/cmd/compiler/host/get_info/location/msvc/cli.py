from pathlib import Path
from typing import NoReturn, Optional, Union

import build_system.cmd.compiler.host.get_info.cli
from build_system.compiler import *
from ext.error import *

from ext.meta_prog.encapsulation import *


def _find_no_arg(compiler_installation_path: Optional[Path] = None) -> Union[Path, NoReturn]:
    compiler_installation_path: Optional[Path] = build_system.cmd.compiler.host.get_info.location.msvc.find_location(compiler_installation_path)

    if compiler_installation_path is None:
        raise CompilerNotFoundError()

    return compiler_installation_path


@export
def find() -> None:
    build_system.cmd.compiler.host.get_info.cli.fetch_compiler_info(CompilerFamily.MSVC,
                                                                    _find_no_arg, desc_compiler_info='location',
                                                                    help_path_meaning='installation')
