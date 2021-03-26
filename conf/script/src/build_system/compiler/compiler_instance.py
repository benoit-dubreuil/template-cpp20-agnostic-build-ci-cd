import dataclasses

import build_system.compiler.family
import build_system.compiler.host.architecture
import build_system.compiler.host.os_family
import build_system.compiler.version


@dataclasses.dataclass(order=True, frozen=True)
class CompilerInstance:
    compiler_family: build_system.compiler.family.CompilerFamily
    os_family: build_system.compiler.host.os_family.OSFamily
    version: build_system.compiler.version.CompilerVersion

    @classmethod
    def create_from_installed_compiler(cls,
                                       compiler_family: build_system.compiler.family.CompilerFamily,
                                       os_family: build_system.compiler.host.os_family.OSFamily,
        import build_system.cmd.compiler.host.get_info.version.fetch_by_criteria

        version = build_system.cmd.compiler.host.get_info.version.fetch_by_criteria.fetch_by_compiler_family(compiler_family)
        return cls(compiler_family=compiler_family, os_family=os_family, version=version, installation_path=installation_path)
