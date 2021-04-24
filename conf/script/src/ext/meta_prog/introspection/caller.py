__all__ = ['get_nth_caller', 'get_caller', 'is_caller_main']

import inspect
from types import FrameType
from typing import Final

from .macro import *

CALLER_MIN_N: Final[int] = 1


def get_nth_caller(n: int = CALLER_MIN_N) -> FrameType:
    assert n >= CALLER_MIN_N

    stack_indices = range(CALLER_MIN_N, n)
    caller_frame: FrameType = inspect.currentframe()

    for _ in stack_indices:
        caller_frame = caller_frame.f_back

    return caller_frame


def get_caller() -> FrameType:
    return get_nth_caller(n=CALLER_MIN_N + 1)


def is_frame_main(frame: FrameType) -> bool:
    frame_script_name = frame.f_locals[Macro.NAME]
    return frame_script_name == Macro.MAIN


def is_caller_main() -> bool:
    caller = get_caller()
    return is_frame_main(frame=caller)