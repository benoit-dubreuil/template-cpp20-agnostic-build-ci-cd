import build_system.build_target.build_type
import build_system.build_target.name
import build_system.compiler.installed_instance


def _assemble_target_build_types() -> list[build_system.build_target.build_type.TargetBuildType]:
    return list(build_system.build_target.build_type.TargetBuildType)


def _fetch_supported_compiler_instance() -> list[build_system.compiler.installed_instance.CompilerInstance]:
    import build_system.cmd.hierarchy.create_target_build_dirs.required_host_info

    os_family = build_system.cmd.hierarchy.create_target_build_dirs.required_host_info.fetch_os_family()
    return build_system.cmd.hierarchy.create_target_build_dirs.required_host_info.fetch_supported_compiler_instances_by_os(os_family)


def generate_target_build_dir_names() -> list[str]:
    import build_system.cmd.hierarchy.create_target_build_dirs.required_host_info

    supported_compiler_instances = _fetch_supported_compiler_instance()
    target_build_types = _assemble_target_build_types()
    arch = build_system.cmd.hierarchy.create_target_build_dirs.required_host_info.detect_arch()

    build_dir_names = []
    for compiler_instance in supported_compiler_instances:
        for target_build_type in target_build_types:
            target_name = build_system.build_target.name.TargetBuildName(compiler_instance=compiler_instance, arch=arch, target_build_type=target_build_type)
            build_dir_names.append(str(target_name))

    return build_dir_names
