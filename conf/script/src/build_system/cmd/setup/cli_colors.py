import colorama

from utils.more_typing import PathLike


def colorize_label(label: str) -> None:
    return colorama.Fore.CYAN + label + colorama.Style.RESET_ALL


def colorize_path(path_info: PathLike) -> None:
    return colorama.Fore.LIGHTBLACK_EX + path_info + colorama.Style.RESET_ALL
