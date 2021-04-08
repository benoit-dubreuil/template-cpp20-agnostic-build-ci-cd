import colorama


def colorize_label(label: str) -> None:
    return colorama.Fore.CYAN + label + colorama.Style.RESET_ALL
