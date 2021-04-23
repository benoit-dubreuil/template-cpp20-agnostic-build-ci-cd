__all__ = ['no_export']

import inspect

from ..introspection import *


# TODO : Do not empty __all__. Create an empty if non-existant, else assure that func is absent
def no_export(func):
    module = inspect.getmodule(func)
    module_api = TAlias_Macro_All()

    setattr(module, Macro.ALL, module_api)

    return func
