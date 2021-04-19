from dataclasses import dataclass
from typing import final

from ..core import *
from .gnu import *

from ext.meta_prog.encapsulation import *


@export
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
