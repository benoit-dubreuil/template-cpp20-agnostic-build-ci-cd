__all__ = ['UTF_8']

from encodings import utf_8
from typing import Final

UTF_8: Final[str] = utf_8.getregentry().name
