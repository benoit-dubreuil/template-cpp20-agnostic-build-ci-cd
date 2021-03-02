#!/usr/bin/env python3

import platform


def generate_build_dir_name():
    system_name = platform.system()
    return system_name.lower()


build_dir_name = generate_build_dir_name()
print(build_dir_name)
