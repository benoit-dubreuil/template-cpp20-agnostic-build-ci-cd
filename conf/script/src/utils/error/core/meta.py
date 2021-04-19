import abc

from ...meta_prog.encapsulation import *


@export
class ErrorMeta(abc.ABCMeta, type):

    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
