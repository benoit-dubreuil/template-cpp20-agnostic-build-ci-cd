import inspect


# https://stackoverflow.com/a/35710527/2924010
def export(func):
    module = inspect.getmodule(func)
    if hasattr(module, '__all__'):
        module.__all__.append(func.__name__)
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
