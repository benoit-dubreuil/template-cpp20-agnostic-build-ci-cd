__all__ = ['GCCCompilerInstance']

from dataclasses import dataclass
from typing import final

from .gnu import *
from ..core import *


@final
@dataclass(order=True, frozen=True)
class GCCCompilerInstance(GNUCompilerInstance):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def get_c_compiler_name() -> str:
        return r'gcc'

    @staticmethod
    def get_cpp_compiler_name() -> str:
        return r'g++'

    @staticmethod
    def get_supported_compiler_families() -> list[CompilerFamily]:
        return [CompilerFamily.GCC]
