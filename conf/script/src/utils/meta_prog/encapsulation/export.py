import inspect


# https://stackoverflow.com/a/35710527/2924010
def export(fn):
    module = inspect.getmodule(fn)
    if hasattr(module, '__all__'):
        module.__all__.append(fn.__name__)
    else:
        module.__all__ = [fn.__name__]
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
