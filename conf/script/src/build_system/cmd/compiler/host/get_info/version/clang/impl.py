__all__ = ['fetch_clang_version']

from build_system.compiler import *
from ..gnu import *


def fetch_clang_version() -> CompilerVersion:
    return fetch_gnu_version(CompilerFamily.CLANG.value)
