import abc
import types
from typing import Callable, Optional, Type, Union

import utils.error.cli_exit
import utils.error.format
import utils.error.meta
import utils.error.status


# noinspection PyAbstractClass
class ManagedErrorMixin(utils.error.status.EncodedErrorMixin, utils.error.cli_exit.ExitCLIErrorMixin, utils.error.format.BaseFormattedErrorMixin,
                        metaclass=utils.error.meta.ErrorMeta):


class ManageClass:

    def __new__(cls, decorated_cls: Optional[type] = None, error_formatter_cls: Type[utils.error.format.BaseFormattedErrorMixin] = utils.error.format.FormattedErrorMixin,
                encoded_error_status: Optional[utils.error.status.ErrorStatus] = None) -> Union[type, Callable[[Optional[type]], type]]:
        # noinspection PyAbstractClass
        class DecoratedManagedErrorAPIMixin(error_formatter_cls, ManagedErrorMixin):
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
