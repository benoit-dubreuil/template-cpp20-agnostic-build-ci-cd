from typing import Final, Optional

import build_system.build_target.build_target
import build_system.build_target.compiler_instance_targets
import build_system.compiler.build_option.build_type
import build_system.compiler.installed_instance
import build_system.compiler.supported_installed_instances
import utils.error.cls_def
from build_system.compiler.build_option.sanitizer import CompilerSanitizer


def checked_generate_targets(compiler_instances: Optional[list[build_system.compiler.installed_instance.CompilerInstance]] = None) \
        -> list[build_system.build_target.compiler_instance_targets.CompilerInstanceTargets]:
    targets = generate_targets(compiler_instances=compiler_instances)

    if len(targets) <= 0:
        raise utils.error.cls_def.NoSupportedCompilersAvailableError()

    return targets


def generate_targets(compiler_instances: Optional[list[build_system.compiler.installed_instance.CompilerInstance]] = None) \
        -> list[build_system.build_target.compiler_instance_targets.CompilerInstanceTargets]:
    compiler_instances = _get_compiler_instances(compiler_instances=compiler_instances)
    build_types = _get_build_types()
    targets = _generate_targets(compiler_instances=compiler_instances, build_types=build_types)

    return targets


def _get_compiler_instances(compiler_instances: Optional[list[build_system.compiler.installed_instance.CompilerInstance]] = None) \
        -> list[build_system.compiler.installed_instance.CompilerInstance]:
    if compiler_instances is None:
        fetched_compiler_instances = build_system.compiler.supported_installed_instances.fetch_all()
    else:
        fetched_compiler_instances = compiler_instances

    return fetched_compiler_instances


def _get_build_types() -> list[build_system.compiler.build_option.build_type.TargetBuildType]:
    return list(build_system.compiler.build_option.build_type.TargetBuildType)


def _generate_targets(compiler_instances: list[build_system.compiler.installed_instance.CompilerInstance],
                      build_types: list[build_system.compiler.build_option.build_type.TargetBuildType]) \
        -> list[build_system.build_target.compiler_instance_targets.CompilerInstanceTargets]:
    targets: list[build_system.build_target.compiler_instance_targets.CompilerInstanceTargets] = []

    for compiler_instance in compiler_instances:
        targets_of_compiler_instance = _generate_targets_of_compiler_instance(compiler_instance=compiler_instance, build_types=build_types)

        targets.append(targets_of_compiler_instance)

    return targets


def _generate_targets_of_compiler_instance(compiler_instance: build_system.compiler.installed_instance.CompilerInstance,
                                           build_types: list[build_system.compiler.build_option.build_type.TargetBuildType]) \
        -> build_system.build_target.compiler_instance_targets.CompilerInstanceTargets:
    supported_sanitizers: Final[list[CompilerSanitizer]] = compiler_instance.get_supported_sanitizers()
    build_targets: list[build_system.build_target.build_target.BuildTarget] = []

    for build_type in build_types:
        for sanitizer in supported_sanitizers:
            build_target = build_system.build_target.build_target.BuildTarget(compiler_instance=compiler_instance,
                                                                              target_build_type=build_type,
                                                                              sanitizer=sanitizer)
            build_targets.append(build_target)

    targets_of_compiler_instance = build_system.build_target.compiler_instance_targets.CompilerInstanceTargets(compiler_instance=compiler_instance,
                                                                                                               build_targets=build_targets)
    return targets_of_compiler_instance
