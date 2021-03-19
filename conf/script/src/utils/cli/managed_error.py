import abc
from typing import Type

import utils.cli.error_meta
import utils.error.error_status
import utils.error.format


class ManagedError(abc.ABC, utils.error.error_status.EncodedError, utils.error.format.BaseFormattedError, metaclass=utils.cli.error_meta.ErrorMeta):
    ...


def manage(cls: type, error_formatter_cls: Type[utils.error.format.BaseFormattedError] = utils.error.format.FormattedError):
    class NewlyManagedError(cls, ManagedError, error_formatter_cls, metaclass=utils.cli.error_meta.ErrorMeta):
        ...

    return NewlyManagedError
