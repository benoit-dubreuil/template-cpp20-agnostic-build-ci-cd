__all__ = ['cli_fetch_clang_version']

from build_system.compiler import *
from ..gnu import *


def cli_fetch_clang_version() -> None:
    cli_fetch_gnu_version(compiler_family=CompilerFamily.CLANG)
