from typing import Final

import build_system.cmd.setup.build_type
import build_system.cmd.setup.required_host_info
import build_system.compiler.family
import build_system.compiler.host.architecture
import build_system.compiler.host.os_family
import build_system.compiler.version


def assemble_build_types() -> list[build_system.cmd.setup.build_type.BuildType]:
    return list(build_system.cmd.setup.build_type.BuildType)


def generate_build_subdir_name(os_family: build_system.compiler.host.os_family.OSFamily,
                               compiler_family: build_system.compiler.family.CompilerFamily,
                               compiler_version: build_system.compiler.version.CompilerVersion,
                               arch: build_system.compiler.host.architecture.Architecture,
                               build_type: build_system.cmd.setup.build_type.BuildType) -> str:
    sep: Final = '-'

    os_family_name = os_family.value
    arch_bit_name = arch.arch_to_bit_name()
    compiler_name = compiler_family.value
    compiler_version_name = str(compiler_version)
    build_type_name = build_type.value

    return os_family_name + sep + arch_bit_name + sep + compiler_name + sep + compiler_version_name + sep + build_type_name


def generate_all_build_subdir_names() -> list[str]:
    os_family = build_system.cmd.setup.required_host_info.fetch_os_family()
    supported_compiler_instances = build_system.cmd.setup.required_host_info.fetch_supported_compiler_instances_by_os(os_family)
    all_build_types = assemble_build_types()
    arch = build_system.cmd.setup.required_host_info.detect_arch()

    build_dir_names = []
    for compiler_instance in supported_compiler_instances:
        for build_type in all_build_types:
            generated = generate_build_subdir_name(os_family, compiler_instance.compiler_family, compiler_instance.version, arch, build_type)
            build_dir_names.append(generated)

    return build_dir_names
