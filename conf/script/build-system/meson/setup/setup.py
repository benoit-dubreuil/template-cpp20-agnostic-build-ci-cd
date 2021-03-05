#!/usr/bin/env python3

from typing import Final
from pprint import pp
import sys
import platform

from data_model import *
from compiler_reqs import CompilerReqs


def fetch_os_name() -> str:
    return platform.system().lower()


def detect_arch() -> Architecture:
    exclusive_max_word = sys.maxsize + 1
    word_size = exclusive_max_word.bit_length()

    return Architecture(word_size)


def arch_to_bit_name(arch: Architecture) -> str:
    return str(arch.value) + 'bit'


def fetch_arch_bit_name() -> str:
    return arch_to_bit_name(detect_arch())


def assemble_build_types() -> list[BuildType]:
    return [p_build_type.value for p_build_type in BuildType]


def generate_build_dir_name(build_type: BuildType) -> str:
    sep: Final = '-'

    os_simple_name = fetch_os_name()
    arch_bit_name = fetch_arch_bit_name()

    return os_simple_name + sep + arch_bit_name + sep + build_type.value


def generate_all_build_dir_names() -> list[str]:
    all_build_types = assemble_build_types()
    return [generate_build_dir_name(build_type) for build_type in all_build_types]


all_build_dir_names = generate_all_build_dir_names()
print(*all_build_dir_names, sep='\n')

all_compilers_reqs = CompilerReqs.create_all_from_file()
pp(all_compilers_reqs)
