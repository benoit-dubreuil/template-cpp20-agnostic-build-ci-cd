from dataclasses import dataclass

from build_system.compiler.family import CompilerFamily
from build_system.compiler.host.os_family import OSFamily
from build_system.compiler.version import CompilerVersion
import build_system.cmd.compiler.host.get_info.version


@dataclass(order=True, frozen=True)
class CompilerInstance:
    compiler_family: CompilerFamily
    os_families: list[OSFamily]
    version: CompilerVersion

    @classmethod
    def create_from_installed_compiler(cls, compiler_family: CompilerFamily, os_family: OSFamily) -> 'CompilerInstance':
        version = build_system.cmd.compiler.host.get_info.version.fetch_by_compiler_family(compiler_family)
        return cls(compiler_family=compiler_family, os_families=[os_family], version=version)

    def get_current_os_family(self) -> build_system.compiler.host.os_family.OSFamily:
        return self.os_families[0]
