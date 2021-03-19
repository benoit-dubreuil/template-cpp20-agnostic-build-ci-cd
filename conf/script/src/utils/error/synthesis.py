from typing import Final, Type

import utils.error.error
import utils.error.status
import utils.error.manage

ALL_ERRORS: Final[list[Type[utils.cli.managed_error.ManagedError]]] = [
    utils.error.error.SuccessWarning,
    utils.error.error.UnsupportedError,
    utils.error.error.ArgParserError,
    utils.error.error.UnknownParsedArgError,
    utils.error.error.EmptyParsedArgError,
    utils.error.error.RootDirNotFoundError,
    utils.error.error.BuildDirNotFoundError,
]

ALL_ERRORS_BY_STATUS: Final[dict[utils.error.status.ErrorStatus, Type[utils.cli.managed_error.ManagedError]]] = {status: ALL_ERRORS[status] for status in
                                                                                                                 utils.error.status.ErrorStatus}
