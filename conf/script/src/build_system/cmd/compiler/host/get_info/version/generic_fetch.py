from pathlib import Path
from typing import AnyStr, Callable

import build_system.compiler.version
import utils.cmd_integrity
import utils.error.core.cls_def


def assure_path_integrity(compiler_path: Path) -> None:
    """Assures the integrity of the supplied :param:`compiler_path`

    :param compiler_path: The path to the compiler executable file. It must not be a directory.
    """
    if not utils.cmd_integrity.cmd_exists(str(compiler_path)):
        raise utils.error.core.cls_def.CompilerNotFoundError()


def interpret_fetched_version(compiler_version_str: AnyStr) -> build_system.compiler.version.CompilerVersion:
    return build_system.compiler.version.CompilerVersion.create_from_str(compiler_version_str.strip())


def fetch(compiler: Path, fetch_compiler_version_func: Callable[[Path], AnyStr]) -> build_system.compiler.version.CompilerVersion:
    compiler_version_str: AnyStr = fetch_compiler_version_func(compiler)
    return interpret_fetched_version(compiler_version_str)
