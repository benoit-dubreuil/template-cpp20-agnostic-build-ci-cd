from dataclasses import dataclass

from .build_target import *
from ..compiler import *

from ext.meta_prog.encapsulation import *


@export
@dataclass(order=True, frozen=True)
class CompilerInstanceTargets:
    compiler_instance: CompilerInstance
    build_targets: list[BuildTarget]

    def __iter__(self):
        return self.build_targets.__iter__()
