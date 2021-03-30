import dataclasses

import build_system.build_target.name
import build_system.compiler.installed_instance


@dataclasses.dataclass(order=True, frozen=True)
class CompilerInstanceTargets:
    compiler_instance: build_system.compiler.installed_instance.CompilerInstance
    targets: list[build_system.build_target.name.TargetBuildName]

    def __init__(self,
                 compiler_instance: build_system.compiler.installed_instance.CompilerInstance,
                 targets: list[build_system.build_target.name.TargetBuildName] = None) -> None:
        assert compiler_instance is not None

        object.__setattr__(self, 'compiler_instance', compiler_instance)

        if targets is None:
            object.__setattr__(self, 'targets', [])
        else:
            object.__setattr__(self, 'targets', targets)

    def __iter__(self):
        return self.targets
