from typing import Final

import utils.error.cls_def
import utils.error.status

ALL_ERRORS: Final = [
    utils.error.cls_def.SuccessWarning,
    utils.error.cls_def.UnsupportedError,
    utils.error.cls_def.ArgParserError,
    utils.error.cls_def.UnknownParsedArgError,
    utils.error.cls_def.EmptyParsedArgError,
    utils.error.cls_def.RootDirNotFoundError,
    utils.error.cls_def.BuildDirNotFoundError,
]

ALL_ERRORS_BY_STATUS: Final = {status: ALL_ERRORS[status] for status in utils.error.status.ErrorStatus}
