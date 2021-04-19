import encodings
from typing import Final

import ext.cli.arg

DIR_STR: Final[str] = 'dir'
ROOT_STR: Final[str] = 'root'
BUILD_SYSTEM_NAME: Final[str] = 'meson'

BUILD_SYSTEM_CONF_FILE_NAME: Final[str] = f'{BUILD_SYSTEM_NAME}.build'

BUILD_DIR_NAME: Final[str] = 'build'
TARGET_SCRIPT_DIR_NAME = 'script'
TARGET_SCRIPT_EXPORT_SHELL_ENV_NAME = 'export_shell_env'
TARGET_SCRIPT_COMPILER_ENV_NAME = 'compiler_env.properties'

CONF_DIR_NAME: Final[str] = 'conf'
CONF_BUILD_SYSTEM_DIR_NAME: Final[str] = f'{BUILD_DIR_NAME}-system'
MESON_MACHINE_FILES_DIR_NAME: Final[str] = 'machine'

ROOT_DIR_ARG: Final[ext.cli.arg.CLIArg] = ext.cli.arg.CLIArg(f'{ROOT_STR}{DIR_STR}')
BUILD_DIR_ARG: Final[ext.cli.arg.CLIArg] = ext.cli.arg.CLIArg(f'{BUILD_DIR_NAME}{DIR_STR}')

BUILD_DIR_PERMISSIONS: Final[int] = 0o770
UTF_8: Final[str] = encodings.utf_8.getregentry().name
