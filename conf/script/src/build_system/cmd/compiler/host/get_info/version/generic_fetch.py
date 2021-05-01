__all__ = ['verify_compiler_path',
           'interpret_fetched_compiler_version',
           'fetch_compiler_version']

from pathlib import Path
from typing import AnyStr, Callable

from build_system.compiler import *
from error import *
from ext.utils.path import *


def verify_compiler_path(compiler_path: Path) -> None:
    """Assures the integrity of the supplied :param:`compiler_path`

    :param compiler_path: The path to the compiler executable file. It must not be a directory.
    """
    if not cmd_exists(str(compiler_path)):
        raise CompilerNotFoundError()


def interpret_fetched_compiler_version(compiler_version_str: AnyStr) -> CompilerVersion:
    return CompilerVersion.create_from_str(compiler_version_str.strip())


def fetch_compiler_version(compiler: Path, fetch_compiler_version_func: Callable[[Path], AnyStr]) -> CompilerVersion:
    compiler_version_str: AnyStr = fetch_compiler_version_func(compiler)
    return interpret_fetched_compiler_version(compiler_version_str)
