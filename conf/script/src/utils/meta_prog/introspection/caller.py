import inspect
from types import FrameType
from typing import Final

CALLER_MIN_N: Final[int] = 1


def get_nth_caller(n: int = CALLER_MIN_N) -> FrameType:
    assert n >= CALLER_MIN_N

    stack_indices = range(CALLER_MIN_N, n)
    caller_frame: FrameType = inspect.currentframe()

    for _ in stack_indices:
        caller_frame = caller_frame.f_back

    return caller_frame
