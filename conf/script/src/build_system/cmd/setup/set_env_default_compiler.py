import contextlib
import os


class EnvDefaultCompiler(contextlib.AbstractContextManager):

    def __enter__(self):
        ...

    def __exit__(self, exc_type, exc_value, traceback):
        ...
