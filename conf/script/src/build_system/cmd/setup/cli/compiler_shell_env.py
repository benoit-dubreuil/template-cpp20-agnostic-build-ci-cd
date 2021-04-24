from typing import Final

from build_system.build_target import *


def print_symlink_to_compiler_export_shell_env_script(target: BuildTarget) -> None:
    from build_system.cmd.setup.cli.colorize import colorize_label, colorize_path

    label: Final[str] = colorize_label(label='Symlink to compiler export shell env script') + ': '

    colorized_symlink = colorize_path(path_info=target.export_shell_env_symlink)

    print(label, end=str())
    print(colorized_symlink)
