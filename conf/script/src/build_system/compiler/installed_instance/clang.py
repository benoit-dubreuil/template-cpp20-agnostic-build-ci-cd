from dataclasses import dataclass
from typing import final

import build_system.compiler.family
import build_system.compiler.installed_instance.gnu


@final
@dataclass(order=True, frozen=True)
class ClangCompilerInstance(build_system.compiler.installed_instance.gnu.GNUCompilerInstance):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def get_c_compiler_name() -> str:
        return r'clang'

    @staticmethod
    def get_cpp_compiler_name() -> str:
        return r'clang++'

    @staticmethod
    def get_supported_compiler_families() -> list[build_system.compiler.family.CompilerFamily]:
        return [build_system.compiler.family.CompilerFamily.CLANG]
