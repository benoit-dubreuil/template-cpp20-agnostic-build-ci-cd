from typing import Final

from build_system.build_target import *


def print_compiler_env_file(target: BuildTarget) -> None:
    from build_system.cmd.setup.cli.colorize import colorize_label, colorize_path

    label: Final[str] = colorize_label(label='Compiler env') + ': '

    colorized_symlink = colorize_path(path_info=target.compiler_env_file)

    print(label, end=str())
    print(colorized_symlink)
