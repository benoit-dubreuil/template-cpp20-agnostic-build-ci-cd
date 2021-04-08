#!/usr/bin/env python3

import venv
from pathlib import Path
from typing import Final

ROOT_DIR: Final[Path] = Path().absolute()
ROOT_DIR.resolve(strict=True)

SCRIPT_DIR: Final[Path] = ROOT_DIR / Path('conf') / 'script'
SCRIPT_DIR.resolve(strict=True)

REQS_FILE: Final[Path] = SCRIPT_DIR / 'requirements.txt'
REQS_FILE.resolve(strict=True)

VENV_DIR: Final[Path] = ROOT_DIR / 'venv'
VENV_PIP_DIR: Final[Path] = VENV_DIR / 'Lib' / 'site-packages' / 'pip'

venv.create(env_dir=VENV_DIR,
            system_site_packages=False,
            clear=True,
            symlinks=False,  # See Windows warning https://docs.python.org/3/library/venv.html#creating-virtual-environments
            with_pip=True,
            upgrade_deps=True)


def pip_install_reqs() -> None:
    ...