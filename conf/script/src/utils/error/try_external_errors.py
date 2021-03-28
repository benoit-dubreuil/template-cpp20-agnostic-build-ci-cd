from typing import Callable


def try_manage_external_errors(func_to_try: Callable, external_errors_to_manage: [Exception] = [Exception]):
    assert func_to_try is not None
    assert external_errors_to_manage is not None
    assert len(external_errors_to_manage) > 0
    