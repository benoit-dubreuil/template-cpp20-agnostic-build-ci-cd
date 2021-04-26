__all__ = ['CompilerInstanceTargets']

from dataclasses import dataclass

from .build_target_cls import *
from ..compiler import *


@dataclass(order=True, frozen=True)
class CompilerInstanceTargets:
    compiler_instance: CompilerInstance
    build_targets: list[BuildTarget]

    def __iter__(self):
        return self.build_targets.__iter__()
