import build_system.cmd.compiler.host.get_info.version.clang
import build_system.cmd.compiler.host.get_info.version.gcc
import build_system.cmd.compiler.host.get_info.version.msvc
import build_system.compiler.core.family
import build_system.compiler.core.version

fetch_func_by_compiler_family = {build_system.compiler.core.family.CompilerFamily.MSVC: build_system.cmd.compiler.host.get_info.version.msvc.fetch_version,
                                 build_system.compiler.core.family.CompilerFamily.CLANG: build_system.cmd.compiler.host.get_info.version.clang.fetch_clang_version,
                                 build_system.compiler.core.family.CompilerFamily.GCC: build_system.cmd.compiler.host.get_info.version.gcc.fetch_gcc_version}


def fetch_by_compiler_family(compiler_family: build_system.compiler.core.family.CompilerFamily) -> build_system.compiler.core.version.CompilerVersion:
    return fetch_func_by_compiler_family[compiler_family]()
