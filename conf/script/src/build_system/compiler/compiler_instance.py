from dataclasses import dataclass

from build_system.compiler.family import CompilerFamily
from build_system.compiler.host.os_family import OSFamily
from build_system.compiler.version import CompilerVersion


@dataclass(order=True, frozen=True)
class CompilerInstance:
    compiler_family: CompilerFamily
    os_families: list[OSFamily]
    version: CompilerVersion
