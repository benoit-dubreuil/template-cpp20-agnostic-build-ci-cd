#!/usr/bin/env python3

import types
import venv
from pathlib import Path
from typing import Final

ROOT_DIR: Final[Path] = Path().absolute()
ROOT_DIR.resolve(strict=True)

SCRIPT_DIR: Final[Path] = ROOT_DIR / Path('conf') / 'script'
SCRIPT_DIR.resolve(strict=True)

REQS_FILE: Final[Path] = SCRIPT_DIR / 'requirements.txt'
REQS_FILE.resolve(strict=True)

VENV_SUPPLIED_DIR: Final[Path] = ROOT_DIR / 'venv'


class EnvBuilderInstallReqs(venv.EnvBuilder):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def post_setup(self, context: types.SimpleNamespace) -> None:
        module_option: Final[str] = '-m'
        pip_arg: Final[str] = 'pip'
        pip_install_arg: Final[str] = 'install'
        pip_install_reqs_option: Final[str] = '-r'

        venv_python = str(context.env_exe)

        pip_cmd_args: list[str] = [venv_python,
                                   module_option,
                                   pip_arg,
                                   pip_install_arg,
                                   pip_install_reqs_option,
                                   REQS_FILE]
        ...


venv_builder = EnvBuilderInstallReqs(system_site_packages=False,
                                     clear=True,
                                     with_pip=True,
                                     upgrade_deps=True)

venv_builder.create(env_dir=VENV_SUPPLIED_DIR)
