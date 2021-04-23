import encodings
import typing

import ext.cli.arg

_TAlias_Const = typing.Final[str]
_TAlias_CLI_Const = typing.Final[ext.cli.arg.CLIArg]

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
MESON_MACHINE_FILES_DIR_NAME: _TAlias_Const = 'machine'

ROOT_DIR_ARG: _TAlias_CLI_Const = ext.cli.arg.CLIArg(f'{ROOT_STR}{DIR_STR}')
BUILD_DIR_ARG: _TAlias_CLI_Const = ext.cli.arg.CLIArg(f'{BUILD_DIR_NAME}{DIR_STR}')

BUILD_DIR_PERMISSIONS: typing.Final[int] = 0o770
UTF_8: _TAlias_Const = encodings.utf_8.getregentry().name
