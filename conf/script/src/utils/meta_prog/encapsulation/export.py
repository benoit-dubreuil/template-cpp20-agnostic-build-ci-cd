import inspect

from utils.meta_prog.introspection import *

__all__: TAlias_Macro_All = ['export']


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
