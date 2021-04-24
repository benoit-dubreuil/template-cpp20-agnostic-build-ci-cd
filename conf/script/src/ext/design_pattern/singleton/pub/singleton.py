__all__ = ['SingletonMixin']

from typing import ClassVar, Optional
from abc import ABCMeta


class SingletonMixin(metaclass=ABCMeta):
    __singleton: ClassVar[Optional['SingletonMixin']] = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def get_singleton(cls, *args, **kwargs) -> 'SingletonMixin':
        if cls.__singleton is None:
            cls._force_create_singleton(*args, **kwargs)

        return cls.__singleton

    @classmethod
    def _force_create_singleton(cls, *args, **kwargs) -> None:
        cls.__singleton = cls(*args, **kwargs)
