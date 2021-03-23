from typing import Final

import build_system.build_target.build_type
import build_system.build_target.target_name
import build_system.cmd.setup.required_host_info
import build_system.compiler.family
import build_system.compiler.host.architecture
import build_system.compiler.host.os_family
import build_system.compiler.version


def assemble_target_build_types() -> list[build_system.build_target.build_type.TargetBuildType]:
    return list(build_system.build_target.build_type.TargetBuildType)


def generate_all_build_subdir_names() -> list[str]:
    os_family = build_system.cmd.setup.required_host_info.fetch_os_family()
    supported_compiler_instances = build_system.cmd.setup.required_host_info.fetch_supported_compiler_instances_by_os(os_family)
    target_build_types = assemble_target_build_types()
    arch = build_system.cmd.setup.required_host_info.detect_arch()

    build_dir_names = []
    for compiler_instance in supported_compiler_instances:
        for target_build_type in target_build_types:
            target_name = build_system.build_target.target_name.TargetBuildName(compiler_instance=compiler_instance, arch=arch, target_build_type=target_build_type)
            build_dir_names.append(str(target_name))

    return build_dir_names
