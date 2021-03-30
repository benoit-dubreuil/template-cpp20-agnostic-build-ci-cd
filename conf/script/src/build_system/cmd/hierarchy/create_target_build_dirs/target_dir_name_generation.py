import build_system.build_target.build_type
import build_system.build_target.name
import build_system.compiler.installed_instance
import build_system.compiler.supported_installed_instances


def _assemble_target_build_types() -> list[build_system.build_target.build_type.TargetBuildType]:
    return list(build_system.build_target.build_type.TargetBuildType)


def generate_target_build_dir_names(supported_installed_compilers: list[build_system.compiler.installed_instance.CompilerInstance] = None) \
        -> dict[build_system.compiler.installed_instance.CompilerInstance, list[build_system.build_target.build_type.TargetBuildType]]:
    if supported_installed_compilers is None:
        host_compilers = build_system.compiler.supported_installed_instances.fetch_all()
    else:
        host_compilers = supported_installed_compilers

    build_dir_names_by_compiler_instance: dict[build_system.compiler.installed_instance.CompilerInstance, list[build_system.build_target.build_type.TargetBuildType]] = {}
    target_build_types = _assemble_target_build_types()

    for compiler_instance in host_compilers:
        build_dir_names_by_compiler_instance[compiler_instance] = target_build_types

    return build_dir_names_by_compiler_instance
