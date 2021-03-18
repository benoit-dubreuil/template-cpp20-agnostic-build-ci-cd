import abc

import utils.cli.error_meta
import utils.cli.error_status
import utils.format_error


class ManagedError(abc.ABC, utils.cli.error_status.EncodedError, utils.format_error.BaseFormattedError, metaclass=utils.cli.error_meta.ErrorMeta):
    ...
