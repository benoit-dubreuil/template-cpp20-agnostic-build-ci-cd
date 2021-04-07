import colorama


def print_meson_cmd(meson_cli_args: list[str]) -> None:
    meson_cmd = ' '.join(meson_cli_args)
    colored_meson_cmd = colorama.Fore.LIGHTBLACK_EX + meson_cmd + colorama.Style.RESET_ALL

    print(colored_meson_cmd)
