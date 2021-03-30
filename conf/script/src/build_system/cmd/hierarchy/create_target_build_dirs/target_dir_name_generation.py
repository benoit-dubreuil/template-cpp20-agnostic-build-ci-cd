import build_system.build_target.build_target_cls
import build_system.build_target.build_type
import build_system.build_target.compiler_instance_targets
import build_system.build_target.name
import build_system.compiler.installed_instance
import build_system.compiler.supported_installed_instances


def generate_all_compiler_instances_targets(supported_installed_compilers: list[build_system.compiler.installed_instance.CompilerInstance] = None) \
        -> list[build_system.build_target.compiler_instance_targets.CompilerInstanceTargets]:
    host_compilers = _assure_host_compilers_are_fetched(supported_installed_compilers)
    all_target_build_types = _assemble_target_build_types()
    all_compiler_instances_targets = _generate_all_compiler_instances_targets_for_build_types(all_target_build_types, host_compilers)

    return all_compiler_instances_targets


def _assure_host_compilers_are_fetched(supported_installed_compilers):
    if supported_installed_compilers is None:
        host_compilers = build_system.compiler.supported_installed_instances.fetch_all()
    else:
        host_compilers = supported_installed_compilers
    return host_compilers


def _assemble_target_build_types() -> list[build_system.build_target.build_type.TargetBuildType]:
    return list(build_system.build_target.build_type.TargetBuildType)


def _generate_compiler_instance_targets(all_target_build_types, compiler_instance):
    all_targets: list[build_system.build_target.build_target_cls.BuildTarget] = []

    for target_build_type in all_target_build_types:
        target_build_name = build_system.build_target.name.TargetBuildName(compiler_instance=compiler_instance,
                                                                           target_build_type=target_build_type)

        target = build_system.build_target.build_target_cls.BuildTarget(build_name=target_build_name)
        all_targets.append(target)

    compiler_instance_targets = build_system.build_target.compiler_instance_targets.CompilerInstanceTargets(compiler_instance=compiler_instance,
                                                                                                            targets=all_targets)
    return compiler_instance_targets


def _generate_all_compiler_instances_targets_for_build_types(all_target_build_types, host_compilers):
    all_compiler_instances_targets: list[build_system.build_target.compiler_instance_targets.CompilerInstanceTargets] = []

    for compiler_instance in host_compilers:
        compiler_instance_targets = _generate_compiler_instance_targets(all_target_build_types=all_target_build_types,
                                                                        compiler_instance=compiler_instance)

        all_compiler_instances_targets.append(compiler_instance_targets)

    return all_compiler_instances_targets
