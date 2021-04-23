from pathlib import Path
from typing import AnyStr, Callable

from build_system.compiler import *
from ext.cmd_integrity import *
from ext.error import *

from ext.meta_prog.encapsulation import *


@export
def verify_compiler_path(compiler_path: Path) -> None:
    """Assures the integrity of the supplied :param:`compiler_path`

    :param compiler_path: The path to the compiler executable file. It must not be a directory.
    """
    if not ext.cmd_integrity.cmd_exists(str(compiler_path)):
        raise CompilerNotFoundError()


@export
def interpret_fetched_compiler_version(compiler_version_str: AnyStr) -> CompilerVersion:
    return CompilerVersion.create_from_str(compiler_version_str.strip())


@export
def fetch_compiler_version(compiler: Path, fetch_compiler_version_func: Callable[[Path], AnyStr]) -> CompilerVersion:
    compiler_version_str: AnyStr = fetch_compiler_version_func(compiler)
    return interpret_fetched_compiler_version(compiler_version_str)
