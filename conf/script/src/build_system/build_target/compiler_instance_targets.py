import dataclasses

import build_system.build_target.build_target_cls
import build_system.compiler.installed_instance


@dataclasses.dataclass(order=True, frozen=True)
class CompilerInstanceTargets:
    compiler_instance: build_system.compiler.installed_instance.CompilerInstance
    targets: list[build_system.build_target.build_target_cls.BuildTarget]

    def __iter__(self):
        return self.targets
