import abc

from typing import Optional, Type, Callable

import utils.error.format
import utils.error.meta
import utils.error.status


class ManagedError(utils.error.status.EncodedError, utils.error.format.BaseFormattedError, metaclass=utils.error.meta.ErrorMeta):
    ...


class ManageClass:

    def __init__(self, cls_to_decorate: type, error_formatter_cls: Type[utils.error.format.BaseFormattedError] = utils.error.format.FormattedError,
                 encoded_error_status: Optional[utils.error.status.ErrorStatus] = None):
        self.cls_to_decorate = cls_to_decorate
        self.error_formatter_cls = error_formatter_cls

        if [encoded_error_status is not None]:
            self.encoded_error_status = encoded_error_status

    def __call__(self) -> Callable[[], type]:
        def inner_cls():
            # noinspection PyAbstractClass
            class DecoratedManagedError(self.cls_to_decorate, ManagedError, self.error_formatter_cls, metaclass=utils.error.meta.ErrorMeta):
                if hasattr(self, 'encoded_error_status'):
                    @staticmethod
                    def get_error_status() -> utils.error.status.ErrorStatus:
                        return self.encoded_error_status

            return DecoratedManagedError

        return inner_cls
