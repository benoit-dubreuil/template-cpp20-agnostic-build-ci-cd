__all__ = ['export']

import inspect

from ..introspection import *


def export(func):
    module_api: TAlias_Macro_All

    module = inspect.getmodule(func)
    func_api = getattr(func, Macro.QUALNAME)

    if not hasattr(module, Macro.ALL):
        module_api = TAlias_Macro_All()
        setattr(module, Macro.ALL, module_api)
    else:
        module_api = getattr(module, Macro.ALL)

    module_api.append(func_api)

    return func
