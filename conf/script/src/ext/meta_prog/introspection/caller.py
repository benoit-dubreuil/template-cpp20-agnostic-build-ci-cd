__all__ = ['get_nth_caller',
           'get_caller',
           'get_caller_func_name',
           'is_frame_main',
           'is_caller_main']

import inspect
from types import FrameType
from typing import Final

from .macro import *

_CALLER_MIN_N: Final[int] = 1


def get_nth_caller(n: int = _CALLER_MIN_N) -> FrameType:
    assert n >= _CALLER_MIN_N

    caller_index = n + 1
    stack_indices = range(0, caller_index)
    caller_frame: FrameType = inspect.currentframe()

    for _ in stack_indices:
        caller_frame = caller_frame.f_back

    return caller_frame


def get_caller() -> FrameType:
    return get_nth_caller(n=_CALLER_MIN_N + 1)


def get_caller_func_name() -> str:
    return get_caller().f_code.co_name


def is_frame_main(frame: FrameType) -> bool:
    frame_script_name = frame.f_locals[Macro.NAME]
    return frame_script_name == Macro.MAIN


def is_caller_main() -> bool:
    caller = get_caller()
    return is_frame_main(frame=caller)
