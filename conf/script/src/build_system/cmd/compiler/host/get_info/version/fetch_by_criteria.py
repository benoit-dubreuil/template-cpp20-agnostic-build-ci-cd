import build_system.cmd.compiler.host.get_info.version.clang
import build_system.cmd.compiler.host.get_info.version.gcc
import build_system.cmd.compiler.host.get_info.version.msvc
import build_system.compiler.family
import build_system.compiler.version

fetch_func_by_compiler_family = {build_system.compiler.family.CompilerFamily.MSVC: build_system.cmd.compiler.host.get_info.version.msvc.fetch_version,
                                 build_system.compiler.family.CompilerFamily.CLANG: build_system.cmd.compiler.host.get_info.version.clang.fetch,
                                 build_system.compiler.family.CompilerFamily.GCC: build_system.cmd.compiler.host.get_info.version.gcc.fetch_version}


def fetch_by_compiler_family(compiler_family: build_system.compiler.family.CompilerFamily) -> build_system.compiler.version.CompilerVersion:
    return fetch_func_by_compiler_family[compiler_family]()
