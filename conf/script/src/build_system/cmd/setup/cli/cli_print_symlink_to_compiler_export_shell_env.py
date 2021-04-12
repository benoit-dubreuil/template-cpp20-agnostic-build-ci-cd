from typing import Final

import build_system.build_target.build_target


def print_symlink_to_compiler_export_shell_env_script(target: build_system.build_target.build_target.BuildTarget) -> None:
    from build_system.cmd.setup.cli.cli_color import colorize_label, colorize_path

    label: Final[str] = colorize_label(label='Symlink to compiler export shell env vars script') + ': '

    colorized_symlink = colorize_path(path_info=target.export_shell_env_symlink)

    print(label, end=str())
    print(colorized_symlink)
