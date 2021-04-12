from typing import Final

import build_system.build_target.build_target


def print_compiler_env_file(target: build_system.build_target.build_target.BuildTarget) -> None:
    from build_system.cmd.setup.cli.colorize import colorize_label, colorize_path

    label: Final[str] = colorize_label(label='Compiler env') + ': '

    colorized_symlink = colorize_path(path_info=target.compiler_env_file)

    print(label, end=str())
    print(colorized_symlink)
