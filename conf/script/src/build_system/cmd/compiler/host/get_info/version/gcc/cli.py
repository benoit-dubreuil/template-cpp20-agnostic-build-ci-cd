from pathlib import Path
from typing import NoReturn, Optional, Union

import build_system.cmd.compiler.host.get_info.cli
import build_system.cmd.compiler.host.get_info.location.msvc.cli
import build_system.compiler.family
import build_system.compiler.version
import utils.error.cls_def


def fetch_gcc_version() -> None:
    build_system.cmd.compiler.host.get_info.cli.fetch_compiler_info(build_system.compiler.family.CompilerFamily.MSVC, _fetch_version_no_arg, help_path_meaning='installation')
