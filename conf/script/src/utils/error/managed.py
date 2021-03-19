import abc
from typing import Type

import utils.error.meta
import utils.error.status
import utils.error.format


class ManagedError(abc.ABC, utils.error.status.EncodedError, utils.error.format.BaseFormattedError, metaclass=utils.error.meta.ErrorMeta):
    ...


def manage(cls: type, error_formatter_cls: Type[utils.error.format.BaseFormattedError] = utils.error.format.FormattedError):
    def decorator_impl(impl_cls, impl_error_formatter_cls):
        # noinspection PyAbstractClass
        class NewlyManagedError(impl_cls, ManagedError, impl_error_formatter_cls, metaclass=utils.error.meta.ErrorMeta):
            ...

        return NewlyManagedError

    return decorator_impl(cls, error_formatter_cls)
