__all__ = ['print_meson_main_file',
           'print_meson_cmd']

from pathlib import Path
from typing import Final

from file_structure import *
from .colorize import *


def print_meson_main_file(meson_main_file: Path) -> None:
    meson_cmd_label: Final[str] = colorize_label(label=f'{BUILD_SYSTEM_NAME.capitalize()} main file') + ': '
    colorized_meson_main_file = colorize_path(path_info=meson_main_file)

    print(meson_cmd_label, end=str())
    print(colorized_meson_main_file)


def print_meson_cmd(meson_cli_args: list[str]) -> None:
    meson_cmd_label: Final[str] = colorize_label(label=f'{BUILD_SYSTEM_NAME.capitalize()} cmd') + ': '

    meson_cli_cmd_and_args = [BUILD_SYSTEM_NAME, *meson_cli_args]
    meson_cli_full_cmd = ' '.join(meson_cli_cmd_and_args)
    colorized_meson_cmd = colorize_path(path_info=meson_cli_full_cmd)

    print(meson_cmd_label, end=str())
    print(colorized_meson_cmd)
