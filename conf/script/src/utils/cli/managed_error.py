import abc
from typing import Type

import utils.error.error_meta
import utils.error.status
import utils.error.format


class ManagedError(abc.ABC, utils.error.status.EncodedError, utils.error.format.BaseFormattedError, metaclass=utils.error.error_meta.ErrorMeta):
    ...


def manage(cls: type, error_formatter_cls: Type[utils.error.format.BaseFormattedError] = utils.error.format.FormattedError):
    class NewlyManagedError(cls, ManagedError, error_formatter_cls, metaclass=utils.error.error_meta.ErrorMeta):
        ...

    return NewlyManagedError
