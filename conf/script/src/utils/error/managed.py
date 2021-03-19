import abc
import functools

from typing import Optional, Type

import utils.error.format
import utils.error.meta
import utils.error.status


class ManagedError(utils.error.status.EncodedError, utils.error.format.BaseFormattedError, metaclass=utils.error.meta.ErrorMeta):
    ...


def manage(cls: type = None, error_formatter_cls: Type[utils.error.format.BaseFormattedError] = utils.error.format.FormattedError,
           encoded_error_status: Optional[utils.error.status.ErrorStatus] = None):
    @functools.wraps(cls)
    def decorator_impl(impl_cls, impl_error_formatter_cls):
        # noinspection PyAbstractClass
        class NewlyManagedError(impl_cls, ManagedError, impl_error_formatter_cls, metaclass=utils.error.meta.ErrorMeta):
            if encoded_error_status is not None:
                @staticmethod
                def get_error_status() -> utils.error.status.ErrorStatus:
                    return encoded_error_status

        return NewlyManagedError

    return decorator_impl(cls, error_formatter_cls)
