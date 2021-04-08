#!/usr/bin/env python3

import venv
from pathlib import Path
from typing import Final

SCRIPT_DIR: Final[Path] = Path().absolute()
SCRIPT_DIR.resolve(strict=True)

VENV_RELATIVE_DIR: Final[Path] = Path('conf') / 'script' / 'venv'

VENV_DIR: Final[Path] = SCRIPT_DIR / VENV_RELATIVE_DIR
VENV_PIP_DIR: Final[Path] = VENV_DIR / 'Lib' / 'site-packages' / 'pip'

venv.create(env_dir=VENV_DIR,
            system_site_packages=False,
            clear=True,
            symlinks=False,  # See Windows warning https://docs.python.org/3/library/venv.html#creating-virtual-environments
            with_pip=True,
            upgrade_deps=True)

def pip_install_reqs() -> None:
    ...