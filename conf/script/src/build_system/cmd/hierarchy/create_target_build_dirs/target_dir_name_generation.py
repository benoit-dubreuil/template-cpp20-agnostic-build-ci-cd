import build_system.build_target.build_type
import build_system.build_target.name
import build_system.compiler.installed_instance
import build_system.compiler.supported_installed_instances


def _assemble_target_build_types() -> list[build_system.build_target.build_type.TargetBuildType]:
    return list(build_system.build_target.build_type.TargetBuildType)


def generate_target_build_dir_names(supported_installed_compilers: list[build_system.compiler.installed_instance.CompilerInstance] = None) \
        -> list[(str, build_system.compiler.installed_instance.CompilerInstance)]:
    if supported_installed_compilers is None:
        host_compilers = build_system.compiler.supported_installed_instances.fetch_all()
    else:
        host_compilers = supported_installed_compilers

    target_build_types = _assemble_target_build_types()

    build_dir_names = []
    for compiler_instance in host_compilers:
        for target_build_type in target_build_types:
            target_name = build_system.build_target.name.TargetBuildName(compiler_instance=compiler_instance, target_build_type=target_build_type)
            build_dir_names.append(str(target_name))

    return build_dir_names
