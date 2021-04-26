__all__ = ['fetch_compiler_version_by_family']

from build_system.compiler import *
from . import *

_fetch_func = {CompilerFamily.MSVC: fetch_msvc_version,
               CompilerFamily.CLANG: fetch_clang_version,
               CompilerFamily.GCC: fetch_gcc_version}


def fetch_compiler_version_by_family(compiler_family: CompilerFamily) -> CompilerVersion:
    return _fetch_func[compiler_family]()
