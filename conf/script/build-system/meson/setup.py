#!/usr/bin/env python3

import platform
from enum import IntFlag


class Architecture(IntFlag):
    UNKNOWN = 0
    A_16 = 1 << 4
    A_32 = 1 << 5
    A_64 = 1 << 6
    A_128 = 1 << 7


def generate_build_dir_name():
    os_simple_name = platform.system()
    return os_simple_name.lower()


build_dir_name = generate_build_dir_name()
print(build_dir_name)
