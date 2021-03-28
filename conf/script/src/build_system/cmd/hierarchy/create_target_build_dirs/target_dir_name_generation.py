import build_system.build_target.build_type
import build_system.build_target.name
import build_system.compiler.host.architecture
import build_system.compiler.host.os_family
import build_system.compiler.installed_instance
import build_system.compiler.supported_installed_instance.fetch_supported_installed_instances


def _assemble_target_build_types() -> list[build_system.build_target.build_type.TargetBuildType]:
    return list(build_system.build_target.build_type.TargetBuildType)


def _fetch_supported_compiler_instance() -> list[build_system.compiler.installed_instance.CompilerInstance]:
    import build_system.compiler.supported_installed_instance

    os_family = build_system.compiler.host.os_family.fetch_os_family()
    arch = build_system.compiler.host.architecture.detect_arch()

    return build_system.compiler.supported_installed_instance.fetch_by_os(os_family=os_family, arch=arch)


def generate_target_build_dir_names() -> list[str]:
    supported_compiler_instances = _fetch_supported_compiler_instance()
    target_build_types = _assemble_target_build_types()

    build_dir_names = []
    for compiler_instance in supported_compiler_instances:
        for target_build_type in target_build_types:
            target_name = build_system.build_target.name.TargetBuildName(compiler_instance=compiler_instance, target_build_type=target_build_type)
            build_dir_names.append(str(target_name))

    return build_dir_names
