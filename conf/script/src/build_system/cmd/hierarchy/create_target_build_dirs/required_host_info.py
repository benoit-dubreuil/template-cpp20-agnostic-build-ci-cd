import platform
import sys

import build_system.compiler.compiler_instance
import build_system.compiler.host.architecture
import build_system.compiler.host.os_family
import build_system.compiler.reqs.reqs


def fetch_os_name() -> str:
    return platform.system().lower()


def fetch_os_family() -> build_system.compiler.host.os_family.OSFamily:
    # noinspection PyArgumentList
    return build_system.compiler.host.os_family.OSFamily(fetch_os_name())


def fetch_filtered_compilers_reqs_by_os(os_family: build_system.compiler.host.os_family.OSFamily) -> list[build_system.compiler.reqs.reqs.CompilerReqs]:
    all_compilers_reqs = build_system.compiler.reqs.reqs.CompilerReqs.create_all_from_config_file()
    return build_system.compiler.reqs.reqs.CompilerReqs.filter_by_os(all_compilers_reqs, os_family)


def fetch_supported_compiler_instances_by_os(os_family: build_system.compiler.host.os_family.OSFamily) -> list[build_system.compiler.compiler_instance.CompilerInstance]:
    filtered_compiler_reqs = fetch_filtered_compilers_reqs_by_os(os_family)
    supported_compiler_instances: list[build_system.compiler.compiler_instance.CompilerInstance] = list()

    for compiler_reqs in filtered_compiler_reqs:

        if os_family in compiler_reqs.os_families:

            installed_compiler_instance = build_system.compiler.compiler_instance.CompilerInstance.create_from_installed_compiler(compiler_family=compiler_reqs.compiler_family,
                                                                                                                                  os_family=os_family)

            if installed_compiler_instance.version >= compiler_reqs.min_compiler_version:
                supported_compiler_instances.append(installed_compiler_instance)

    return supported_compiler_instances


def detect_arch() -> build_system.compiler.host.architecture.Architecture:
    exclusive_max_word = sys.maxsize + 1
    word_size = exclusive_max_word.bit_length()

    # noinspection PyArgumentList
    return build_system.compiler.host.architecture.Architecture(word_size)
