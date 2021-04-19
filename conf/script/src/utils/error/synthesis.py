from typing import Final

from .cls_def import *
from .status import *

# TODO : Remove, deprecated
ALL_ERRORS: Final = [
    SuccessWarning,
    UnsupportedError,
    ArgParserError,
    UnknownParsedArgError,
    EmptyParsedArgError,
    RootDirNotFoundError,
    BuildDirNotFoundError,
]

ALL_ERRORS_BY_STATUS: Final = {status: ALL_ERRORS[status] for status in ErrorStatus}
