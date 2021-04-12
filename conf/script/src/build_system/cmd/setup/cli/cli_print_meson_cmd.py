from pathlib import Path
from typing import Final

from build_system.cmd.hierarchy.consts import BUILD_SYSTEM_NAME


def print_meson_main_file(meson_main_file: Path) -> None:
    from build_system.cmd.setup.cli.cli_color import colorize_label, colorize_path

    meson_cmd_label: Final[str] = colorize_label(label=f'{BUILD_SYSTEM_NAME.capitalize()} main file') + ': '

    colorized_meson_main_file = colorize_path(path_info=meson_main_file)

    print(meson_cmd_label, end=str())
    print(colorized_meson_main_file)


def print_meson_cmd(meson_cli_args: list[str]) -> None:
    from build_system.cmd.setup.cli.cli_color import colorize_label, colorize_path

    meson_cmd_label: Final[str] = colorize_label(label=f'{BUILD_SYSTEM_NAME.capitalize()} cmd') + ': '

    meson_cli_cmd_and_args = [BUILD_SYSTEM_NAME, *meson_cli_args]
    meson_cli_full_cmd = ' '.join(meson_cli_cmd_and_args)
    colorized_meson_cmd = colorize_path(path_info=meson_cli_full_cmd)

    print(meson_cmd_label, end=str())
    print(colorized_meson_cmd)
