import abc
from typing import Type

import utils.cli.error_meta
import utils.cli.error_status
import utils.format_error


class ManagedError(abc.ABC, utils.cli.error_status.EncodedError, utils.format_error.BaseFormattedError, metaclass=utils.cli.error_meta.ErrorMeta):
    ...


def manage(cls: type, error_formatter_cls: Type[utils.format_error.BaseFormattedError] = utils.format_error.FormattedError):
    class NewlyManagedError(cls, ManagedError, error_formatter_cls, metaclass=utils.cli.error_meta.ErrorMeta):
        ...

    return NewlyManagedError
