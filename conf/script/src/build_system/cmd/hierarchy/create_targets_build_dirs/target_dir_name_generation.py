from typing import Final, Optional

from build_system.build_target import *
from build_system.build_target import *
import build_system.compiler.build_option.build_type
import build_system.compiler.build_option.sanitizer
import build_system.compiler.installed_instance
import build_system.compiler.supported_installed_instances
import ext.error.core.cls_def


def checked_generate_targets(compiler_instances: Optional[list[build_system.compiler.installed_instance.CompilerInstance]] = None) \
        -> list[CompilerInstanceTargets]:
    targets = generate_targets(compiler_instances=compiler_instances)

    if len(targets) <= 0:
        raise ext.error.core.cls_def.NoSupportedCompilersAvailableError()

    return targets


def generate_targets(compiler_instances: Optional[list[build_system.compiler.installed_instance.CompilerInstance]] = None) \
        -> list[CompilerInstanceTargets]:
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
        -> list[CompilerInstanceTargets]:
    targets: list[CompilerInstanceTargets] = []

    for compiler_instance in compiler_instances:
        targets_of_compiler_instance = _generate_targets_of_compiler_instance(compiler_instance=compiler_instance, build_types=build_types)

        targets.append(targets_of_compiler_instance)

    return targets


def _generate_targets_of_compiler_instance(compiler_instance: build_system.compiler.installed_instance.CompilerInstance,
                                           build_types: list[build_system.compiler.build_option.build_type.TargetBuildType]) \
        -> CompilerInstanceTargets:
    build_targets = _generate_build_targets_of_compiler_instance(compiler_instance, build_types)
    targets_of_compiler_instance = CompilerInstanceTargets(compiler_instance=compiler_instance,
                                                                                                               build_targets=build_targets)

    return targets_of_compiler_instance


def _generate_build_targets_of_compiler_instance(compiler_instance: build_system.compiler.installed_instance.CompilerInstance,
                                                 build_types: list[build_system.compiler.build_option.build_type.TargetBuildType]) \
        -> list[BuildTarget]:
    combined_build_options = _combine_build_options(compiler_instance=compiler_instance, build_types=build_types)
    build_targets: list[BuildTarget] = []

    for build_type, sanitizer in combined_build_options:
        build_target = BuildTarget(compiler_instance=compiler_instance,
                                                                          target_build_type=build_type,
                                                                          sanitizer=sanitizer)
        build_targets.append(build_target)

    return build_targets


def _combine_build_options(compiler_instance: build_system.compiler.installed_instance.CompilerInstance,
                           build_types: list[build_system.compiler.build_option.build_type.TargetBuildType]) \
        -> list[tuple[build_system.compiler.build_option.build_type.TargetBuildType, build_system.compiler.build_option.sanitizer.CompilerSanitizer]]:
    supported_sanitizers: Final[list[build_system.compiler.build_option.sanitizer.CompilerSanitizer]] = compiler_instance.get_supported_sanitizers()
    combined_build_options = []

    for build_type in build_types:
        filtered_sanitizers = _filter_sanitizers_by_build_type(build_type=build_type, sanitizers=supported_sanitizers)

        build_options_combination = [build_type] * len(filtered_sanitizers)
        build_options_combination = list(zip(build_options_combination, filtered_sanitizers))

        combined_build_options.extend(build_options_combination)

    return combined_build_options


def _filter_sanitizers_by_build_type(build_type: build_system.compiler.build_option.build_type.TargetBuildType,
                                     sanitizers: list[build_system.compiler.build_option.sanitizer.CompilerSanitizer]) \
        -> list[build_system.compiler.build_option.sanitizer.CompilerSanitizer]:
    if build_type == build_system.compiler.build_option.build_type.TargetBuildType.RELEASE:
        filtered_sanitizers = [build_system.compiler.build_option.sanitizer.CompilerSanitizer.NONE]
    else:
        filtered_sanitizers = sanitizers

    return filtered_sanitizers
