#!/usr/bin/env python3

from configparser import ConfigParser, ExtendedInterpolation

from typing import Final


def filter_config_default_section(config: ConfigParser):
    return list(config.items())[1:]


COMPILER_REQ_FILE: Final = 'compiler-requirements.ini'

config = ConfigParser(interpolation=ExtendedInterpolation())
config.read(COMPILER_REQ_FILE)

filtered_items = filter_config_default_section(config)

[print(item) for item in filtered_items]
