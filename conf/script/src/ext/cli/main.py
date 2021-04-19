from typing import Callable

import colorama

from ..meta_prog.encapsulation import *


@export
def init():
    colorama.init()


@export
def deinit():
    colorama.deinit()


@export
def wrap_main(main_func: Callable):
    init()
    main_func()
    deinit()
