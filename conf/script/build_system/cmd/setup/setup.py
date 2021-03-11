#!/usr/bin/env python3

import platform
import sys
from typing import Final

from build_system import compiler
from build_system.compiler import host
from build_system.cmd.setup.build_type import BuildType
from build_system.compiler.reqs.reqs import CompilerReqs


def fetch_os_name() -> str:
    return platform.system().lower()
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


def generate_build_dir_name(os_family: host.OSFamily, compiler_family: compiler.Family, compiler_version: compiler.Version, arch: host.Architecture, build_type: BuildType) -> str:
    sep: Final = '-'

    os_family_name = os_family.value
    arch_bit_name = arch.arch_to_bit_name()
    compiler_name = compiler_family.value
    compiler_version_name = str(compiler_version)
    build_type_name = build_type.value

    return os_family_name + sep + arch_bit_name + sep + compiler_name + sep + compiler_version_name + sep + build_type_name


def generate_all_build_dir_names() -> list[str]:
    os_family = fetch_os_family()
    filtered_compilers_reqs_by_os = fetch_filtered_compilers_reqs_by_os(os_family)
    all_build_types = assemble_build_types()
    arch = detect_arch()

    build_dir_names = []
    for compiler_reqs in filtered_compilers_reqs_by_os:
        for build_type in all_build_types:
            generated = generate_build_dir_name(os_family, compiler_reqs.compiler, compiler_reqs.version, arch, build_type)
            build_dir_names.append(generated)

    return build_dir_names


all_build_dir_names = generate_all_build_dir_names()
print(*all_build_dir_names, sep='\n', end='')
