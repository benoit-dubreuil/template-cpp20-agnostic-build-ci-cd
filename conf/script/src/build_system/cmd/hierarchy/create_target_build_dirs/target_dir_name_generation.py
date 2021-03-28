import build_system.build_target.build_type
import build_system.build_target.name
import build_system.compiler.host.architecture
import build_system.compiler.host.os_family
import build_system.compiler.installed_instance
import build_system.compiler.supported_installed_instances


def _assemble_target_build_types() -> list[build_system.build_target.build_type.TargetBuildType]:
    return list(build_system.build_target.build_type.TargetBuildType)


def generate_target_build_dir_names() -> list[str]:
    TO_RENAME = build_system.compiler.supported_installed_instances.fetch_all()
    target_build_types = _assemble_target_build_types()

    build_dir_names = []
    for compiler_instance in TO_RENAME:
        for target_build_type in target_build_types:
            target_name = build_system.build_target.name.TargetBuildName(compiler_instance=compiler_instance, target_build_type=target_build_type)
            build_dir_names.append(str(target_name))

    return build_dir_names
