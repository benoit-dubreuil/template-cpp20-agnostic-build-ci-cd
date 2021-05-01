__all__ = ['DIR_STR',
           'ROOT_DIR_ARG',
           'BUILD_DIR_ARG']

from cli import *
from ._type_alias import *
from .fs_build_dir import *
from .fs_root_dir import *

_TAlias_CLI_Arg = Final[CLIArg]

DIR_STR: TAlias_Name = 'dir'

ROOT_DIR_ARG: _TAlias_CLI_Arg = CLIArg(f'{ROOT_STR}{DIR_STR}')
BUILD_DIR_ARG: _TAlias_CLI_Arg = CLIArg(f'{BUILD_STR}{DIR_STR}')
