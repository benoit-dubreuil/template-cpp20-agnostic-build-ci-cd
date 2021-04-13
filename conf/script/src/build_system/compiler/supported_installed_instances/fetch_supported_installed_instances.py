import build_system.compiler.installed_instance
import build_system.compiler.reqs.reqs
import host.architecture
import host.os_family


def _fetch_filtered_compilers_reqs_by_os(os_family: host.os_family.OSFamily) -> list[build_system.compiler.reqs.reqs.CompilerReqs]:
    all_compilers_reqs = build_system.compiler.reqs.reqs.CompilerReqs.create_all_from_config_file()
    return build_system.compiler.reqs.reqs.CompilerReqs.filter_by_os(all_compilers_reqs, os_family)


def fetch_supported_installed_compiler_instances_by_os_and_arch(os_family: host.os_family.OSFamily,
                                                                arch: host.architecture.Architecture) \
        -> list[build_system.compiler.installed_instance.CompilerInstance]:
    filtered_compiler_reqs = _fetch_filtered_compilers_reqs_by_os(os_family)
    supported_compiler_instances: list[build_system.compiler.installed_instance.CompilerInstance] = list()

    for compiler_reqs in filtered_compiler_reqs:

        if os_family in compiler_reqs.os_families:

            installed_compiler_instance = build_system.compiler.installed_instance.CompilerInstance.create_from_installed_compiler(compiler_family=compiler_reqs.compiler_family,
                                                                                                                                   os_family=os_family,
                                                                                                                                   arch=arch)

            if installed_compiler_instance.version >= compiler_reqs.min_compiler_version:
                supported_compiler_instances.append(installed_compiler_instance)

    return supported_compiler_instances


def fetch_supported_installed_compiler_instances() -> list[build_system.compiler.installed_instance.CompilerInstance]:
    os_family = host.os_family.fetch_os_family()
    arch = host.architecture.detect_arch()

    return fetch_supported_installed_compiler_instances_by_os_and_arch(os_family=os_family, arch=arch)
