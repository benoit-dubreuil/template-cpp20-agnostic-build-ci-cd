from pathlib import Path


def print_meson_main_file(meson_main_file: Path) -> None:
    from build_system.cmd.setup.cli_color import colorize_path

    colorized_meson_main_file = colorize_path(path_info=meson_main_file)
    print(colorized_meson_main_file)


def print_meson_cmd(meson_cli_args: list[str]) -> None:
    from build_system.cmd.setup.cli_color import colorize_path

    meson_cmd = ' '.join(meson_cli_args)
    colored_meson_cmd = colorize_path(path_info=meson_cmd)

    print(colored_meson_cmd)
