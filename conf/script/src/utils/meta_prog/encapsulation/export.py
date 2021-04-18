import inspect
import typing


# https://stackoverflow.com/a/35710527/2924010
def export(func):
    attribute_name_all: typing.Final[str] = '__all__'

    module = inspect.getmodule(func)
    func_api = func.__qualname__

    if hasattr(module, attribute_name_all):
        module.__all__.append(func_api)
    else:
        module.__all__ = [func_api]

    print(func)
    print(module)
    print()

    return func


@export
def foo():
    ...


@export
class Bar:
    # @export
    # @staticmethod
    # def __baz():
    #     print('baz')

    ...
