import contextlib
from pathlib import Path
from typing import Final

import mesonbuild.mesonmain

import build_system.build_target.build_target_cls
import build_system.compiler.installed_instance
import utils.cli.hidden_prints
from build_system.cmd.setup.cli_print_target_info import print_target_info


def setup_host_compiler_target_build_dir(root_dir: Path,
                                         host_compiler: build_system.compiler.installed_instance.CompilerInstance,
                                         target_build_dir: build_system.build_target.build_target_cls.BuildTarget,
                                         compiler_env_vars_manager: contextlib.AbstractContextManager,
                                         cli_mode: bool):
    meson_cli_args = _generate_meson_cli_args(root_dir=root_dir,
                                              host_compiler=host_compiler,
                                              target_build_dir=target_build_dir)

    if cli_mode:
        print_target_info(host_compiler=host_compiler,
                          target_build_dir=target_build_dir,
                          compiler_env_vars_manager=compiler_env_vars_manager)

    _run_meson(cli_mode, meson_cli_args)


def _generate_meson_cli_args(root_dir: Path,
                             host_compiler: build_system.compiler.installed_instance.CompilerInstance,
                             target_build_dir: build_system.build_target.build_target_cls.BuildTarget):
    cli_kwarg_assignment_op: Final[str] = r'='

    meson_cli_arg_setup_cmd = r'setup'
    meson_cli_arg_help = r'--help'

    meson_cli_arg_build_type = r'--buildtype' + cli_kwarg_assignment_op + target_build_dir.get_build_type().value
    meson_cli_arg_build_dir = str(target_build_dir.dir)
    meson_cli_arg_source_dir = str(root_dir)

    # TODO : Machine files
    meson_cli_args: list[str] = [meson_cli_arg_setup_cmd,
                                 meson_cli_arg_build_type,
                                 meson_cli_arg_build_dir,
                                 meson_cli_arg_source_dir]

    return meson_cli_args


def _run_meson(cli_mode, meson_cli_args):
    meson_launcher: str = _fetch_meson_launcher()

    try:
        with contextlib.nullcontext() if cli_mode else utils.cli.hidden_prints.HiddenPrints():
            mesonbuild.mesonmain.run(meson_cli_args, meson_launcher)

    except SystemExit:
        pass


def _fetch_meson_launcher() -> str:
    current_package_path = _fetch_current_package_path()
    return str(current_package_path)


def _fetch_current_package_path() -> Path:
    current_package_path = Path(__file__).parent
    current_package_path.resolve(strict=True)
    current_package_path = current_package_path.absolute()

    return current_package_path
