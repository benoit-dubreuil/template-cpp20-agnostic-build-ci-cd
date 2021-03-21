import platform
import sys
from pathlib import Path
from typing import Final, Optional

import build_system.cmd.hierarchy.find_build_dir
import build_system.cmd.hierarchy.find_root_dir
import build_system.cmd.setup.build_type
import build_system.compiler.compiler_instance
import build_system.compiler.host
import build_system.compiler.family
import build_system.compiler.version
import build_system.compiler.reqs.reqs
import utils.error.cls_def

BUILD_DIR_PERMISSIONS: Final[int] = 0o770


def fetch_os_name() -> str:
    return platform.system().lower()


def fetch_os_family() -> build_system.compiler.host.os_family.OSFamily:
    # noinspection PyArgumentList
    return build_system.compiler.host.os_family.OSFamily(fetch_os_name())


def fetch_filtered_compilers_reqs_by_os(os_family: build_system.compiler.host.os_family.OSFamily) -> list[build_system.compiler.reqs.reqs.CompilerReqs]:
    all_compilers_reqs = build_system.compiler.reqs.reqs.CompilerReqs.create_all_from_file()
    return build_system.compiler.reqs.reqs.CompilerReqs.filter_by_os(all_compilers_reqs, os_family)


def fetch_supported_compiler_instances_by_os(os_family: build_system.compiler.host.os_family.OSFamily) -> list[build_system.compiler.compiler_instance.CompilerInstance]:
    filtered_compiler_reqs = fetch_filtered_compilers_reqs_by_os(os_family)
    supported_compiler_instances: list[build_system.compiler.compiler_instance.CompilerInstance] = list()

    for compiler_reqs in filtered_compiler_reqs:

        if os_family in compiler_reqs.compiler_instance.os_families:

            installed_compiler_instance = build_system.compiler.compiler_instance.CompilerInstance.create_from_installed_compiler(
                compiler_family=compiler_reqs.compiler_instance.compiler_family, os_family=os_family)

            if installed_compiler_instance.version >= compiler_reqs.compiler_instance.version:
                supported_compiler_instances += installed_compiler_instance

    return supported_compiler_instances


def detect_arch() -> build_system.compiler.host.architecture.Architecture:
    exclusive_max_word = sys.maxsize + 1
    word_size = exclusive_max_word.bit_length()

    # noinspection PyArgumentList
    return build_system.compiler.host.architecture.Architecture(word_size)


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
    os_family = fetch_os_family()
    supported_compiler_instances = fetch_supported_compiler_instances_by_os(os_family)
    all_build_types = assemble_build_types()
    arch = detect_arch()

    build_dir_names = []
    for compiler_instance in supported_compiler_instances:
        for build_type in all_build_types:
            generated = generate_build_subdir_name(os_family, compiler_instance.compiler_family, compiler_instance.version, arch, build_type)
            build_dir_names.append(generated)

    return build_dir_names


def create_build_subdir(build_dir: Path, build_subdir: str):
    build_subdir_path = build_dir / build_subdir
    build_subdir_path.mkdir(mode=BUILD_DIR_PERMISSIONS, exist_ok=True)


def create_all_build_subdirs(build_dir: Path, all_build_subdirs: list[str]):
    for build_subdir in all_build_subdirs:
        create_build_subdir(build_dir, build_subdir)


def find_or_create_build_dir(root_dir: Optional[Path] = None) -> Path:
    if root_dir is None:
        root_dir = build_system.cmd.hierarchy.find_root_dir.find_root_dir()
    else:
        assert root_dir.exists()

    build_dir = build_system.cmd.hierarchy.find_build_dir.find_build_dir_path(root_dir)

    if build_dir.exists():
        if not build_dir.is_dir():
            raise utils.error.cls_def.RootDirNotFoundError()
    else:
        build_dir.mkdir(mode=BUILD_DIR_PERMISSIONS, parents=True)

    return build_dir


def setup(root_dir: Optional[Path] = None):
    build_dir = find_or_create_build_dir(root_dir)

    all_build_subdir_names = generate_all_build_subdir_names()
    # create_all_build_subdirs(build_dir, all_build_subdir_names)

    # TODO : Remove when #58 is done
    print(*all_build_subdir_names, sep='\n', end=str())
