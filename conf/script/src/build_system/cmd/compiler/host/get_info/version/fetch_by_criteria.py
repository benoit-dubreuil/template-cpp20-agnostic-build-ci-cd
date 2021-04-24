__all__ = ['fetch_by_compiler_family']

from . import *
from build_system.compiler import *

_fetch_func_by_compiler_family = {CompilerFamily.MSVC: fetch_msvc_version,
                                  CompilerFamily.CLANG: fetch_clang_version,
                                  CompilerFamily.GCC: fetch_gcc_version}


def fetch_by_compiler_family(compiler_family: CompilerFamily) -> CompilerVersion:
    return _fetch_func_by_compiler_family[compiler_family]()
