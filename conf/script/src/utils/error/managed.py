import abc
import types
from typing import Optional, Type

import utils.error.format
import utils.error.meta
import utils.error.status


class ManagedError(utils.error.status.EncodedError, utils.error.format.BaseFormattedError, metaclass=utils.error.meta.ErrorMeta):
    ...


class ManageClass:

    def __new__(cls, decorated_cls: Optional[type] = None, error_formatter_cls: Type[utils.error.format.BaseFormattedError] = utils.error.format.FormattedError,
                encoded_error_status: Optional[utils.error.status.ErrorStatus] = None) -> type:
        # noinspection PyAbstractClass
        class DecoratedManagedErrorAPI(ManagedError, error_formatter_cls, metaclass=utils.error.meta.ErrorMeta):
            if encoded_error_status is not None:
                @staticmethod
                def get_error_status() -> utils.error.status.ErrorStatus:
                    return encoded_error_status

        def create_managed_cls(unmanaged_cls: type) -> type:
            managed_class_namespace = {
                '__module__': __name__ if unmanaged_cls.__module__ is None else unmanaged_cls.__module__
            }

            return types.new_class(unmanaged_cls.__qualname__,
                                   bases=(unmanaged_cls, DecoratedManagedErrorAPI),
                                   kwds={'metaclass': utils.error.meta.ErrorMeta},
                                   exec_body=lambda ns: ns.update(managed_class_namespace))

        if decorated_cls is not None:
            return create_managed_cls(decorated_cls)
        else:
            def wrapper(wrapped_decorated_cls):
                return ManageClass(wrapped_decorated_cls, error_formatter_cls, encoded_error_status)

            return wrapper
