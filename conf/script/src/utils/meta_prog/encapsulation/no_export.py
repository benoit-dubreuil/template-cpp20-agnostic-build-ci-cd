__all__ = ['no_export']

import inspect
import typing

from utils.meta_prog.introspection import *


def no_export(func: typing.Callable):
    module = inspect.getmodule(func)
    module_api = TAlias_Macro_All()

    setattr(module, Macro.ALL, module_api)

    return func
