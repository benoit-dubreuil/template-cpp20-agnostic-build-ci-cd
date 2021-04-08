#!/usr/bin/env python3

import venv
import types
from pathlib import Path
from typing import Final

ROOT_DIR: Final[Path] = Path().absolute()
ROOT_DIR.resolve(strict=True)

SCRIPT_DIR: Final[Path] = ROOT_DIR / Path('conf') / 'script'
SCRIPT_DIR.resolve(strict=True)

REQS_FILE: Final[Path] = SCRIPT_DIR / 'requirements.txt'
REQS_FILE.resolve(strict=True)

VENV_SUPPLIED_DIR: Final[Path] = ROOT_DIR / 'venv'

PIP_CMD_ARGS: Final[list[str]] = []


class EnvBuilderInstallReqs(venv.EnvBuilder):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def post_setup(self, context: types.SimpleNamespace):
        ...


venv_builder = EnvBuilderInstallReqs(system_site_packages=False,
                                     clear=True,
                                     with_pip=True,
                                     upgrade_deps=True)

venv_builder.create(env_dir=VENV_SUPPLIED_DIR)
