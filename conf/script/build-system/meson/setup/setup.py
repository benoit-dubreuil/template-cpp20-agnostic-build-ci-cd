#!/usr/bin/env python3

from typing import Final

import sys
import platform

from data_model import *


def detect_arch():
    exclusive_max_word = sys.maxsize + 1
    word_size = exclusive_max_word.bit_length()

    return Architecture(word_size)


def arch_to_bit_name(arch: Architecture):
    return str(arch.value) + 'bit'


def generate_build_dir_name():
    dir_name_separator: Final = '-'

    os_simple_name = platform.system().lower()
    arch_bit_name = arch_to_bit_name(detect_arch())

    return os_simple_name + dir_name_separator + arch_bit_name


build_dir_name = generate_build_dir_name()
print(build_dir_name)
