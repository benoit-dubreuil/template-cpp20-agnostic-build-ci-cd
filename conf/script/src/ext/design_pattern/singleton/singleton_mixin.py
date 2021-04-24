__all__ = ['SingletonMixin']

from abc import ABCMeta
from typing import Callable, ClassVar, Optional, TypeVar

_T = TypeVar('_T', bound='SingletonMixin')


class SingletonMixin(metaclass=ABCMeta):
    __singleton: ClassVar[Optional[_T]] = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def get_singleton(cls, *args, **kwargs) -> _T:
        if cls.__singleton is None:
            cls._force_create_singleton(*args, **kwargs)

        return cls.__singleton

    @classmethod
    def _force_create_singleton(cls, *args, **kwargs) -> None:
        singleton_creator = cls._get_singleton_creator()
        cls.__singleton = singleton_creator(*args, **kwargs)

    @classmethod
    def _get_singleton_creator(cls) -> Callable[..., _T]:
        return cls.__init__
