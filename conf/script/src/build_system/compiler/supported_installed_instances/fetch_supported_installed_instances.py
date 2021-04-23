from ..installed_instance import *
from ..reqs import *
from host import *

from ext.meta_prog.encapsulation import *


def _fetch_filtered_compilers_reqs_by_os(os_family: OSFamily) -> list[CompilerReqs]:
    all_compilers_reqs = CompilerReqs.create_all_from_config_file()
    return CompilerReqs.filter_by_os(all_compilers_reqs, os_family)


@export
def fetch_supported_installed_compiler_instances_by_os_and_arch(os_family: OSFamily,
                                                                arch: Architecture) \
        -> list[CompilerInstance]:
    filtered_compiler_reqs = _fetch_filtered_compilers_reqs_by_os(os_family)
    supported_compiler_instances: list[CompilerInstance] = list()

    for compiler_reqs in filtered_compiler_reqs:

        if os_family in compiler_reqs.os_families:

            installed_compiler_instance = CompilerInstance.create_from_installed_compiler(compiler_family=compiler_reqs.compiler_family,
                                                                                          os_family=os_family,
                                                                                          arch=arch)

            if installed_compiler_instance.version >= compiler_reqs.min_compiler_version:
                supported_compiler_instances.append(installed_compiler_instance)

    return supported_compiler_instances


@export
def fetch_supported_installed_compiler_instances() -> list[CompilerInstance]:
    os_family = OSFamily.detect()
    arch = Architecture.detect_arch()

    return fetch_supported_installed_compiler_instances_by_os_and_arch(os_family=os_family, arch=arch)
