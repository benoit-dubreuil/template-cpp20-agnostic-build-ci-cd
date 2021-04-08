import colorama

from utils.more_typing import PathLike


def colorize_header(header: str) -> str:
    return colorama.Fore.LIGHTCYAN_EX + header + colorama.Style.RESET_ALL


def colorize_label(label: str) -> str:
    return colorama.Fore.CYAN + label + colorama.Style.RESET_ALL


def colorize_path(path_info: PathLike) -> str:
    return colorama.Fore.LIGHTBLACK_EX + str(path_info) + colorama.Style.RESET_ALL
