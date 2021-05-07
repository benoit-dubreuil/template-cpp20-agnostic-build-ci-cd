__all__ = ['setup_target']

import contextlib
import sys
from pathlib import Path
from typing import Final

import mesonbuild.mesonmain

from build_system.build_target import *
from build_system.cmd.setup._priv.cli import *
from build_system.compiler import *
from cli import *
from error import *
from ext.utils.path import *
from file_structure import *
from .meson_machine_file_args import *


def setup_target(root_dir: Path,
                 compiler_instance: CompilerInstance,
                 build_target: BuildTarget,
                 compiler_env_manager: contextlib.AbstractContextManager,
                 cli_mode: bool):
    meson_cli_args = _generate_meson_setup_cli_args(root_dir=root_dir,
                                                    compiler_instance=compiler_instance,
                                                    build_target=build_target)

    if cli_mode:
        print_target_info(compiler_instance=compiler_instance,
                          target=build_target,
                          compiler_env_manager=compiler_env_manager)

        print_meson_cmd(meson_cli_args=meson_cli_args)

    _run_meson(cli_mode, meson_cli_args)


def _generate_meson_setup_cli_args(root_dir: Path,
                                   compiler_instance: CompilerInstance,
                                   build_target: BuildTarget):
    cli_kwarg_assignment_op: Final[str] = r'='

    cli_arg_setup_cmd = r'setup'

    setup_cli_fatal_warnings = r'--fatal-meson-warnings'

    setup_cli_arg_build_dir = str(build_target.dir)
    setup_cli_arg_source_dir = str(root_dir)

    meson_cli_args: list[str] = [cli_arg_setup_cmd,
                                 setup_cli_fatal_warnings,
                                 *(generate_meson_machine_files_args(compiler_instance=compiler_instance, build_target=build_target)),
                                 setup_cli_arg_build_dir,
                                 setup_cli_arg_source_dir]

    return meson_cli_args


def _run_meson(cli_mode, meson_cli_args):
    meson_launcher: str = _find_meson_launcher(cli_mode=cli_mode)

    try:
        with contextlib.nullcontext() if cli_mode else HiddenPrints():
            mesonbuild.mesonmain.run(meson_cli_args, meson_launcher)

    except SystemExit:
        pass


def _find_meson_launcher(cli_mode: bool) -> str:
    venv_interpreter = Path(sys.executable)
    venv_scripts_dir = venv_interpreter.parent

    meson_main_file, meson_main_file_exists = get_cmd_path(cmd=BUILD_SYSTEM_NAME, dir_path=venv_scripts_dir)

    if not meson_main_file_exists:
        raise MesonMainFileNotFoundError()

    if cli_mode:
        print_meson_main_file(meson_main_file=meson_main_file)

    return str(meson_main_file)
