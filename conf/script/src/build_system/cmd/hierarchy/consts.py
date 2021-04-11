from typing import Final

import utils.cli.arg

DIR_STR: Final[str] = 'dir'
ROOT_STR: Final[str] = 'root'
BUILD_SYSTEM_NAME: Final[str] = 'meson'

BUILD_DIR_NAME: Final[str] = 'build'
CONF_DIR_NAME: Final[str] = 'conf'
CONF_BUILD_SYSTEM_DIR_NAME: Final[str] = f'{BUILD_DIR_NAME}-system'
MESON_MACHINE_FILES_DIR_NAME: Final[str] = 'machine'
TARGET_SCRIPT_DIR_NAME = 'script'
TARGET_SCRIPT_EXPORT_SHELL_ENV_VARS_NAME = 'export_shell_env_vars'

ROOT_DIR_ARG: Final[utils.cli.arg.CLIArg] = utils.cli.arg.CLIArg(f'{ROOT_STR}{DIR_STR}')
BUILD_DIR_ARG: Final[utils.cli.arg.CLIArg] = utils.cli.arg.CLIArg(f'{BUILD_DIR_NAME}{DIR_STR}')

BUILD_DIR_PERMISSIONS: Final[int] = 0o770

BUILD_SYSTEM_CONF_FILE_NAME: Final[str] = f'{BUILD_SYSTEM_NAME}.build'
