__all__ = ['print_compiler_env_file']

from typing import Final

from build_system.build_target import *
from .colorize import *


def print_compiler_env_file(target: BuildTarget) -> None:
    label: Final[str] = colorize_label(label='Compiler env') + ': '
    colorized_symlink = colorize_path(path_info=target.compiler_env_file)

    print(label, end=str())
    print(colorized_symlink)
