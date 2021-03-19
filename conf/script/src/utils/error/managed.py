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

        def populate_namespace(namespace):
            return namespace

        return types.new_class(cls_to_decorate.__name__,
                               (cls_to_decorate, DecoratedManagedErrorAPI),
                               {'metaclass': utils.error.meta.ErrorMeta},
                               populate_namespace)
