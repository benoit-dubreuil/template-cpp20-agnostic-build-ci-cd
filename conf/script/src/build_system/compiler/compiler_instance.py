import dataclasses

import build_system.cmd.compiler.host.get_info.version
import build_system.compiler
import build_system.compiler.host


@dataclasses.dataclass(order=True, frozen=True)
class CompilerInstance:
    compiler_family: build_system.compiler.family.CompilerFamily
    os_families: list[build_system.compiler.host.OSFamily]
    version: build_system.compiler.version.CompilerVersion

    @classmethod
    def create_from_installed_compiler(cls, compiler_family: build_system.compiler.family.CompilerFamily, os_family: build_system.compiler.host.OSFamily) -> 'CompilerInstance':
        version = build_system.cmd.compiler.host.get_info.version.fetch_by_compiler_family(compiler_family)
        return cls(compiler_family=compiler_family, os_families=[os_family], version=version)

    def get_current_os_family(self) -> build_system.compiler.host.OSFamily:
        return self.os_families[0]
