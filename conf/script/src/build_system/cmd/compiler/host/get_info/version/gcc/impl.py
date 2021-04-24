__all__ = ['fetch_gcc_version']

from build_system.compiler import *
from ..gnu import *


def fetch_gcc_version() -> CompilerVersion:
    return fetch_gnu_version(CompilerFamily.GCC.value)
