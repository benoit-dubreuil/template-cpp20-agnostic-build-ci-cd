from typing import Final, Type

import utils.cli.error
import utils.error.status
import utils.error.managed_error

ALL_ERRORS: Final[list[Type[utils.cli.managed_error.ManagedError]]] = [
    utils.cli.error.SuccessWarning,
    utils.cli.error.UnsupportedError,
    utils.cli.error.ArgParserError,
    utils.cli.error.UnknownParsedArgError,
    utils.cli.error.EmptyParsedArgError,
    utils.cli.error.RootDirNotFoundError,
    utils.cli.error.BuildDirNotFoundError,
]

ALL_ERRORS_BY_STATUS: Final[dict[utils.error.status.ErrorStatus, Type[utils.cli.managed_error.ManagedError]]] = {status: ALL_ERRORS[status] for status in
                                                                                                                 utils.error.status.ErrorStatus}
