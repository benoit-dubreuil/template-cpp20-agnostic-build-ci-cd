import inspect


# https://stackoverflow.com/a/35710527/2924010
def export(fn):
    mod = inspect.getmodule(fn)
    if hasattr(mod, '__all__'):
        mod.__all__.append(fn.__name__)
    else:
        mod.__all__ = [fn.__name__]
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
