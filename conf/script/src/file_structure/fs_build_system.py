__all__ = ['SYSTEM_STR',
           'BUILD_SYSTEM_NAME',
           'BUILD_SYSTEM_CONF_FILE_EXTENSION',
           'BUILD_SYSTEM_CONF_FILE_NAME']

from ._type_alias import *
from .fs_build_dir import *

SYSTEM_STR: TAlias_Name = 'system'
BUILD_SYSTEM_NAME: TAlias_Name = 'meson'

BUILD_SYSTEM_CONF_FILE_EXTENSION: TAlias_Name = BUILD_STR
BUILD_SYSTEM_CONF_FILE_NAME: TAlias_Name = f'{BUILD_SYSTEM_NAME}.{BUILD_SYSTEM_CONF_FILE_EXTENSION}'
