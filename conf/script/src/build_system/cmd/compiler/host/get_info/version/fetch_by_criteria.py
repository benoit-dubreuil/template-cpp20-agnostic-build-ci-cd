__all__ = ['fetch_func_by_compiler_family']

from . import *
from build_system.compiler import *

fetch_func_by_compiler_family = {build_system.compiler.family.CompilerFamily.MSVC: build_system.cmd.compiler.host.get_info.version.msvc.fetch_version,
                                 build_system.compiler.family.CompilerFamily.CLANG: build_system.cmd.compiler.host.get_info.version.clang.fetch_version,
                                 build_system.compiler.family.CompilerFamily.GCC: build_system.cmd.compiler.host.get_info.version.gcc.fetch_version}

fetch_func_by_compiler_family = {CompilerFamily.MSVC: fetch_msvc_version,
                                 CompilerFamily.CLANG: fetch_clang_version,
                                 CompilerFamily.GCC: fetch_gcc_version}


@export
def fetch_by_compiler_family(compiler_family: CompilerFamily) -> CompilerVersion:
    return fetch_func_by_compiler_family[compiler_family]()
