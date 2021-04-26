__all__ = ['CONF_DIR_NAME',
           'CONF_BUILD_SYSTEM_DIR_NAME',
           'CONF_MESON_MACHINE_FILES_DIR_NAME']

from ._type_alias import *
from .build_dir import *
from .build_system import *

CONF_DIR_NAME: TAlias_Name = 'conf'
CONF_BUILD_SYSTEM_DIR_NAME: TAlias_Name = f'{BUILD_DIR_NAME}-{SYSTEM_STR}'
CONF_MESON_MACHINE_FILES_DIR_NAME: TAlias_Name = 'machine'
