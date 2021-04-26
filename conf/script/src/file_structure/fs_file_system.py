__all__ = ['BUILD_DIR_PERMISSIONS',
           'UTF_8']

from encodings import utf_8

from ._type_alias import *

BUILD_DIR_PERMISSIONS: Final[int] = 0o770
UTF_8: TAlias_Name = utf_8.getregentry().name
