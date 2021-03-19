from pathlib import Path
from typing import AnyStr, Callable

import utils.cmd_integrity
import utils.error.cls_def
from build_system.compiler.version import CompilerVersion


def assure_path_integrity(compiler_path: Path) -> None:
    """Assures the integrity of the supplied :param:`compiler_path`

    :param compiler_path: The path to the compiler executable file. It must not be a directory.
    """
    if not utils.cmd_integrity.cmd_exists(str(compiler_path)):
        raise utils.error.cls_def.CompilerNotFoundError()


def interpret_fetched_version(compiler_version_str: AnyStr) -> CompilerVersion:
    return CompilerVersion.create_from_str(compiler_version_str.strip())


def fetch(compiler: Path, fetch_compiler_version_func: Callable[[Path], AnyStr]) -> CompilerVersion:
    compiler_version_str: AnyStr = fetch_compiler_version_func(compiler)
    return interpret_fetched_version(compiler_version_str)
