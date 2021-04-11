#!/usr/bin/env python3

import subprocess
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

VENV_SUPPLIED_DIR: Final[Path] = SCRIPT_DIR / 'venv'


class EnvBuilderInstallReqs(venv.EnvBuilder):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def upgrade_dependencies(self, context: types.SimpleNamespace) -> None:
        print(f'Upgrade dependecies : pip, setuptools')
        print('-------------------------------------')

        super().upgrade_dependencies(context=context)

        self.__install_reqs(context=context)

    @classmethod
    def __install_reqs(cls, context: types.SimpleNamespace) -> None:
        pip_cmd_args: list[str] = cls.__assemble_pip_cmd_args(context=context)

        print()
        print('Install requirements.txt using pip')
        print('----------------------------------')

        subprocess.check_call(pip_cmd_args)

    @staticmethod
    def __assemble_pip_cmd_args(context: types.SimpleNamespace) -> list[str]:
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

        return pip_cmd_args


venv_builder = EnvBuilderInstallReqs(system_site_packages=False,
                                     clear=True,
                                     with_pip=True,
                                     upgrade_deps=True)

venv_builder.create(env_dir=VENV_SUPPLIED_DIR)
