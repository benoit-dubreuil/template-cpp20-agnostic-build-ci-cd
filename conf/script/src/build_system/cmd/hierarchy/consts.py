from typing import Final

import utils.cli.arg

ROOT_DIR_ARG: Final[utils.cli.arg.CLIArg] = utils.cli.arg.CLIArg('rootdir')
BUILD_DIR_NAME: Final[str] = 'build'
BUILD_DIR_PERMISSIONS: Final[int] = 0o770
