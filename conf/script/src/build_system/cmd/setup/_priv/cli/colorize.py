__all__ = ['colorize_header_label',
           'colorize_label',
           'colorize_path']

import colorama

from ext.utils.path import *


def colorize_header_label(header: str) -> str:
    return colorama.Fore.LIGHTCYAN_EX + header + colorama.Style.RESET_ALL


def colorize_label(label: str) -> str:
    return colorama.Fore.CYAN + label + colorama.Style.RESET_ALL


def colorize_path(path_info: TUnion_PathLike) -> str:
    return colorama.Fore.LIGHTBLACK_EX + str(path_info) + colorama.Style.RESET_ALL
