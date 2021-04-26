__all__ = ['generate_targets']

from typing import Final, Optional

from build_system.build_target import *
from build_system.compiler import *
from error import *


def generate_targets(compiler_instances: Optional[list[CompilerInstance]] = None) \
        -> list[CompilerInstanceTargets]:
    targets = _unchecked_generate_targets(compiler_instances=compiler_instances)

    if len(targets) <= 0:
        raise NoSupportedCompilersAvailableError()

    return targets


def _unchecked_generate_targets(compiler_instances: Optional[list[CompilerInstance]] = None) \
        -> list[CompilerInstanceTargets]:
    compiler_instances = _get_compiler_instances(compiler_instances=compiler_instances)
    build_types = _get_build_types()
    targets = _generate_targets(compiler_instances=compiler_instances, build_types=build_types)

    return targets


def _get_compiler_instances(compiler_instances: Optional[list[CompilerInstance]] = None) \
        -> list[CompilerInstance]:
    if compiler_instances is None:
        fetched_compiler_instances = fetch_supported_installed_compiler_instances()
    else:
        fetched_compiler_instances = compiler_instances

    return fetched_compiler_instances


def _get_build_types() -> list[TargetBuildType]:
    return list(TargetBuildType)


def _generate_targets(compiler_instances: list[CompilerInstance],
                      build_types: list[TargetBuildType]) \
        -> list[CompilerInstanceTargets]:
    targets: list[CompilerInstanceTargets] = []

    for compiler_instance in compiler_instances:
        targets_of_compiler_instance = _generate_targets_of_compiler_instance(compiler_instance=compiler_instance, build_types=build_types)

        targets.append(targets_of_compiler_instance)

    return targets


def _generate_targets_of_compiler_instance(compiler_instance: CompilerInstance,
                                           build_types: list[TargetBuildType]) \
        -> CompilerInstanceTargets:
    build_targets = _generate_build_targets_of_compiler_instance(compiler_instance, build_types)
    targets_of_compiler_instance = CompilerInstanceTargets(compiler_instance=compiler_instance,
                                                           build_targets=build_targets)

    return targets_of_compiler_instance


def _generate_build_targets_of_compiler_instance(compiler_instance: CompilerInstance,
                                                 build_types: list[TargetBuildType]) \
        -> list[BuildTarget]:
    combined_build_options = _combine_build_options(compiler_instance=compiler_instance, build_types=build_types)
    build_targets: list[BuildTarget] = []

    for build_type, sanitizer in combined_build_options:
        build_target = BuildTarget(compiler_instance=compiler_instance,
                                   target_build_type=build_type,
                                   sanitizer=sanitizer)
        build_targets.append(build_target)

    return build_targets


def _combine_build_options(compiler_instance: CompilerInstance,
                           build_types: list[TargetBuildType]) \
        -> list[tuple[TargetBuildType, CompilerSanitizer]]:
    supported_sanitizers: Final[list[CompilerSanitizer]] = compiler_instance.get_supported_sanitizers()
    combined_build_options = []

    for build_type in build_types:
        filtered_sanitizers = _filter_sanitizers_by_build_type(build_type=build_type, sanitizers=supported_sanitizers)

        build_options_combination = [build_type] * len(filtered_sanitizers)
        build_options_combination = list(zip(build_options_combination, filtered_sanitizers))

        combined_build_options.extend(build_options_combination)

    return combined_build_options


def _filter_sanitizers_by_build_type(build_type: TargetBuildType,
                                     sanitizers: list[CompilerSanitizer]) \
        -> list[CompilerSanitizer]:
    if build_type == TargetBuildType.RELEASE:
        filtered_sanitizers = [CompilerSanitizer.NONE]
    else:
        filtered_sanitizers = sanitizers

    return filtered_sanitizers
