from . import *
from build_system.compiler import *

from ext.meta_prog.encapsulation import *
from ext.meta_prog.introspection import *

__all__: TAlias_Macro_All = ['fetch_func_by_compiler_family']

fetch_func_by_compiler_family = {CompilerFamily.MSVC: fetch_msvc_version,
                                 CompilerFamily.CLANG: fetch_clang_version,
                                 CompilerFamily.GCC: fetch_gcc_version}


@export
def fetch_by_compiler_family(compiler_family: CompilerFamily) -> CompilerVersion:
    return fetch_func_by_compiler_family[compiler_family]()
