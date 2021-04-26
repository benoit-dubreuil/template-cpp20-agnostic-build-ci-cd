__all__ = ['ErrorMeta']

from abc import ABCMeta


class ErrorMeta(ABCMeta, type):

    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
