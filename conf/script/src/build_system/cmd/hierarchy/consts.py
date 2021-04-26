__all__ = ['DIR_STR',
           'ROOT_STR',
           'BUILD_SYSTEM_NAME',
           'BUILD_SYSTEM_CONF_FILE_NAME',
           'BUILD_DIR_NAME',
           'TARGET_SCRIPT_DIR_NAME',
           'TARGET_SCRIPT_EXPORT_SHELL_ENV_NAME',
           'TARGET_SCRIPT_COMPILER_ENV_NAME',
           'CONF_DIR_NAME',
           'CONF_BUILD_SYSTEM_DIR_NAME',
           'CONF_MESON_MACHINE_FILES_DIR_NAME',
           'ROOT_DIR_ARG',
           'BUILD_DIR_ARG',
           'BUILD_DIR_PERMISSIONS',
           'UTF_8']

from encodings import utf_8
from typing import Final

from ext.cli import *

_TAlias_Const = Final[str]
_TAlias_CLI_Const = Final[CLIArg]

DIR_STR: _TAlias_Const = 'dir'
ROOT_STR: _TAlias_Const = 'root'
BUILD_SYSTEM_NAME: _TAlias_Const = 'meson'

BUILD_SYSTEM_CONF_FILE_NAME: _TAlias_Const = f'{BUILD_SYSTEM_NAME}.build'

BUILD_DIR_NAME: _TAlias_Const = 'build'
TARGET_SCRIPT_DIR_NAME = 'script'
TARGET_SCRIPT_EXPORT_SHELL_ENV_NAME = 'export_shell_env'
TARGET_SCRIPT_COMPILER_ENV_NAME = 'compiler_env.properties'

CONF_DIR_NAME: _TAlias_Const = 'conf'
CONF_BUILD_SYSTEM_DIR_NAME: _TAlias_Const = f'{BUILD_DIR_NAME}-system'
CONF_MESON_MACHINE_FILES_DIR_NAME: _TAlias_Const = 'machine'

ROOT_DIR_ARG: _TAlias_CLI_Const = CLIArg(f'{ROOT_STR}{DIR_STR}')
BUILD_DIR_ARG: _TAlias_CLI_Const = CLIArg(f'{BUILD_DIR_NAME}{DIR_STR}')

BUILD_DIR_PERMISSIONS: Final[int] = 0o770
UTF_8: _TAlias_Const = utf_8.getregentry().name
