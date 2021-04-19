import inspect

from utils.meta_prog.introspection import *

__all__: TAlias_Macro_All = ['no_export']


# TODO : Do not empty __all__. Create an empty if non-existant, else assure that func is absent
def no_export(func):
    module = inspect.getmodule(func)
    module_api = TAlias_Macro_All()

    setattr(module, Macro.ALL, module_api)

    return func
