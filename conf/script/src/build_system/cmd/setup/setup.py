import platform
import sys
from pathlib import Path
from typing import Final, Optional

import build_system.cmd.hierarchy.find_build_dir
import build_system.cmd.hierarchy.find_root_dir
import utils.error.cls_def
from build_system import cmd, compiler
from build_system.cmd.setup.build_type import BuildType
from build_system.compiler import host
from build_system.compiler.reqs.reqs import CompilerReqs


def fetch_os_name() -> str:
    return platform.system().lower()


def fetch_os_family() -> host.OSFamily:
    return host.OSFamily(fetch_os_name())


def fetch_filtered_compilers_reqs_by_os(os_family: host.OSFamily) -> list[CompilerReqs]:
    all_compilers_reqs = CompilerReqs.create_all_from_file()
    return CompilerReqs.filter_by_os(all_compilers_reqs, os_family)


def detect_arch() -> host.Architecture:
    exclusive_max_word = sys.maxsize + 1
    word_size = exclusive_max_word.bit_length()

    return host.Architecture(word_size)


def assemble_build_types() -> list[BuildType]:
    return list(BuildType)


def generate_build_subdir_name(os_family: host.OSFamily, compiler_family: compiler.Family, compiler_version: compiler.Version, arch: host.Architecture, build_type: BuildType) -> str:
    sep: Final = '-'

    os_family_name = os_family.value
    arch_bit_name = arch.arch_to_bit_name()
    compiler_name = compiler_family.value
    compiler_version_name = str(compiler_version)
    build_type_name = build_type.value

    return os_family_name + sep + arch_bit_name + sep + compiler_name + sep + compiler_version_name + sep + build_type_name


def generate_all_build_subdir_names() -> list[str]:
    os_family = fetch_os_family()
    filtered_compilers_reqs_by_os = fetch_filtered_compilers_reqs_by_os(os_family)
    all_build_types = assemble_build_types()
    arch = detect_arch()

    build_dir_names = []
    for compiler_reqs in filtered_compilers_reqs_by_os:
        for build_type in all_build_types:
            generated = generate_build_subdir_name(os_family, compiler_reqs.compiler, compiler_reqs.version, arch, build_type)
            build_dir_names.append(generated)

    return build_dir_names


def find_or_create_build_dir(root_dir: Optional[Path] = None) -> Path:
    if root_dir is None:
        root_dir = cmd.hierarchy.find_root_dir.find_root_dir()
    else:
        assert root_dir.exists()

    build_dir = cmd.hierarchy.find_build_dir.find_build_dir_path(root_dir)

    if build_dir.exists():
        if not build_dir.is_dir():
            raise utils.error.cls_def.RootDirNotFoundError()
    else:
        build_dir.mkdir(mode=0o770, parents=True)

    return root_dir


def setup(root_dir: Optional[Path] = None):
    find_or_create_build_dir(root_dir)

    all_build_dir_names = generate_all_build_subdir_names()

    print(*all_build_dir_names, sep='\n', end=str())
