__all__ = ['print_symlink_to_compiler_export_shell_env_script']

from typing import Final

from build_system.build_target import *
from .colorize import *


def print_symlink_to_compiler_export_shell_env_script(target: BuildTarget) -> None:
    label: Final[str] = colorize_label(label='Symlink to compiler export shell env script') + ': '
    colorized_symlink = colorize_path(path_info=target.export_shell_env_symlink)

    print(label, end=str())
    print(colorized_symlink)
