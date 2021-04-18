from typing import Callable

import colorama


def init():
    colorama.init()


def deinit():
    colorama.deinit()


def wrap_main(main_func: Callable):
    init()
    main_func()
    deinit()
