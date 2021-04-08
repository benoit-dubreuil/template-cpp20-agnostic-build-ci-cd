#!/usr/bin/env python3

import venv
from pathlib import Path
from typing import Final

SCRIPT_DIR: Final[Path] = Path().absolute()
SCRIPT_DIR.resolve(strict=True)

VENV_RELATIVE_DIR: Final[Path] = Path('conf') / 'script' / 'venv'

VENV_DIR: Final[Path] = SCRIPT_DIR / VENV_RELATIVE_DIR

if __name__ == '__main__':
    print('WIP')

# py -m venv . --upgrade-deps --clear
