import inspect
from types import FrameType
from typing import AnyStr, Callable, Final, cast

import colorama

DEFAULT_PATH_ARG_NAME: Final[str] = 'path'
DEFAULT_PATH_ARG: Final[str] = '-' + DEFAULT_PATH_ARG_NAME

MACRO___NAME__: Final[str] = '__name__'
MACRO___NAME___MAIN: Final[str] = '__main__'


def init():
    colorama.init()


def deinit():
    colorama.deinit()


def format_error_msg(error_msg: AnyStr) -> AnyStr:
    return colorama.Style.BRIGHT + colorama.Fore.RED + error_msg + colorama.Style.RESET_ALL


def is_caller_main() -> bool:
    # See https://stackoverflow.com/a/57712700/
    caller_frame = cast(FrameType, cast(FrameType, inspect.currentframe()).f_back)
    caller_script_name = caller_frame.f_locals[MACRO___NAME__]

    return caller_script_name == MACRO___NAME___MAIN


def wrap_main(main_func: Callable):
    init()
    main_func()
    deinit()
