__all__ = ['cli_fetch_gcc_version']

from build_system.compiler import *
from ..gnu import *


def cli_fetch_gcc_version() -> None:
    cli_fetch_gnu_version(compiler_family=CompilerFamily.GCC)
