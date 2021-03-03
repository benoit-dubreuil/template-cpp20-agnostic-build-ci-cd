#!/usr/bin/env python3

from typing import Final

import sys
import platform

from data_model import *


def fetch_os_name():
    return platform.system().lower()


def detect_arch():
    exclusive_max_word = sys.maxsize + 1
    word_size = exclusive_max_word.bit_length()

    return Architecture(word_size)


def arch_to_bit_name(arch: Architecture):
    return str(arch.value) + 'bit'


def fetch_arch_bit_name():
    return arch_to_bit_name(detect_arch())


def assemble_build_types():
    return [p_build_type.value for p_build_type in BuildType]


def generate_build_dir_name(build_type):
    sep: Final = '-'

    os_simple_name = fetch_os_name()
    arch_bit_name = fetch_arch_bit_name()

    return os_simple_name + sep + arch_bit_name + sep + build_type


def generate_all_build_dir_names():
    all_build_types = assemble_build_types()
    return [generate_build_dir_name(build_type) for build_type in all_build_types]


all_build_dir_names = generate_all_build_dir_names()
print(*all_build_dir_names, sep='\n')
