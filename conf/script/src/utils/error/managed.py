import abc
import types
from typing import Any, Optional, Type

import utils.error.format
import utils.error.meta
import utils.error.status


class ManagedError(utils.error.status.EncodedError, utils.error.format.BaseFormattedError, metaclass=utils.error.meta.ErrorMeta):
    ...


class ManageClass:

    def __new__(cls, cls_to_decorate, error_formatter_cls: Type[utils.error.format.BaseFormattedError] = utils.error.format.FormattedError,
                encoded_error_status: Optional[utils.error.status.ErrorStatus] = None) -> Any:
        # noinspection PyAbstractClass
        class DecoratedManagedErrorAPI(ManagedError, error_formatter_cls, metaclass=utils.error.meta.ErrorMeta):
            if encoded_error_status is not None:
                @staticmethod
                def get_error_status() -> utils.error.status.ErrorStatus:
                    return encoded_error_status

        DecoratorModuleSetter = {
            '__module__': __name__ if cls_to_decorate.__module__ is None else cls_to_decorate.__module__
        }

        return types.new_class(cls_to_decorate.__qualname__,
                               bases=(cls_to_decorate, DecoratedManagedErrorAPI),
                               kwds={'metaclass': utils.error.meta.ErrorMeta},
                               exec_body=lambda ns: ns.update(DecoratorModuleSetter))
