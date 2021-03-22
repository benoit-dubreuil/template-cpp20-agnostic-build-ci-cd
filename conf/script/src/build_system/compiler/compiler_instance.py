import dataclasses

import build_system.compiler.family
import build_system.compiler.host
import build_system.compiler.version


@dataclasses.dataclass(order=True, frozen=True)
class CompilerInstance:
    compiler_family: build_system.compiler.family.CompilerFamily
    os_families: list[build_system.compiler.host.os_family.OSFamily]
    version: build_system.compiler.version.CompilerVersion

    @classmethod
    def create_from_installed_compiler(cls,
                                       compiler_family: build_system.compiler.family.CompilerFamily,
                                       os_family: build_system.compiler.host.os_family.OSFamily) -> 'CompilerInstance':
        import build_system.cmd.compiler.host.get_info.version
        
        version = build_system.cmd.compiler.host.get_info.version.fetch_by_compiler_family(compiler_family)
        return cls(compiler_family=compiler_family, os_families=[os_family], version=version)

    def get_current_os_family(self) -> build_system.compiler.host.os_family.OSFamily:
        return self.os_families[0]
