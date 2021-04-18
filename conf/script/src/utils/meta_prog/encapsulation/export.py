import inspect
import typing


def export(func):
    attribute_name_all: typing.Final[str] = '__all__'
    module_api: list[str]

    module = inspect.getmodule(func)
    func_api = func.__qualname__

    if not hasattr(module, attribute_name_all):
        module_api = []
        setattr(module, attribute_name_all, module_api)
    else:
        module_api = getattr(module, attribute_name_all)

    module_api.append(func_api)


    return func


@export
def foo():
    ...


@export
class Bar:

    @staticmethod
    @export
    def __baz():
        print('baz')
