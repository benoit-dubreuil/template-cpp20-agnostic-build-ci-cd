from dataclasses import dataclass

from build_system.compiler.family import CompilerFamily
from build_system.compiler.host.os_family import OSFamily
from build_system.compiler.version import CompilerVersion


@dataclass(order=True, frozen=True)
class CompilerInstance:
    compiler: CompilerFamily
    os_families: list[OSFamily]
    version: CompilerVersion

    @classmethod
    def filter_by_os(cls, all_compilers_reqs: dict[CompilerFamily, 'CompilerReqs'], os_family: OSFamily) -> list['CompilerReqs']:
        return [compiler_reqs for compiler, compiler_reqs in all_compilers_reqs.items() if os_family in compiler_reqs.os_families]
