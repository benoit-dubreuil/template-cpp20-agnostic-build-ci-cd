import dataclasses

import build_system.compiler.installed_instance
import build_system.build_target.name


@dataclasses.dataclass(order=True, frozen=True)
class CompilerInstanceTargets:
    compiler_instance: build_system.compiler.installed_instance.CompilerInstance
    targets: list[build_system.build_target.name.TargetBuildName]
