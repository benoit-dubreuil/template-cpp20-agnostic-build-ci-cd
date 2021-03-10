#!/usr/bin/env python3

import platform
import sys
from typing import Final

from compiler_reqs import CompilerReqs
from compiler_version import CompilerVersion
from data_model import *


def fetch_os_name() -> str:
    return platform.system().lower()


def fetch_os_family() -> OSFamily:
    return OSFamily(fetch_os_name())


def fetch_filtered_compilers_reqs_by_os(os_family: OSFamily) -> list[CompilerReqs]:
    all_compilers_reqs = CompilerReqs.create_all_from_file()
    return CompilerReqs.filter_by_os(all_compilers_reqs, os_family)


def detect_arch() -> Architecture:
    exclusive_max_word = sys.maxsize + 1
    word_size = exclusive_max_word.bit_length()

    return Architecture(word_size)


def assemble_build_types() -> list[BuildType]:
    return list(BuildType)


def generate_build_dir_name(os_family: OSFamily, compiler: Compiler, compiler_version: CompilerVersion, arch: Architecture, build_type: BuildType) -> str:
    sep: Final = '-'

    os_family_name = os_family.value
    arch_bit_name = arch.arch_to_bit_name()
    compiler_name = compiler.value
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
