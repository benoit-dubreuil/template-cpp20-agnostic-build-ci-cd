import inspect
import typing


# https://stackoverflow.com/a/35710527/2924010
def export(func):
    attribute_name_all: typing.Final[str] = '__all__'

    module = inspect.getmodule(func)

    if hasattr(module, attribute_name_all):
        module.__all__.append(func.__qualname__)
    else:
        module.__all__ = [func.__name__]
    return fn


@export
def foo():
    ...


@export
class Bar:

    @export
    @staticmethod
    def __baz():
        print('baz')
