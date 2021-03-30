from dataclasses import dataclass

import build_system.compiler.family
import build_system.compiler.installed_instance.gnu


@dataclass(order=True, frozen=True)
class ClangCompilerInstance(build_system.compiler.installed_instance.gnu.GNUCompilerInstance):

    @staticmethod
    def get_c_compiler_name() -> str:
        return r'clang'

    @staticmethod
    def get_cpp_compiler_name() -> str:
        return r'clang++'

    @staticmethod
    def get_supported_compiler_families() -> list[build_system.compiler.family.CompilerFamily]:
        return [build_system.compiler.family.CompilerFamily.CLANG]
