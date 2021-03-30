from pathlib import Path
from typing import Final

import mesonbuild.mesonmain

import build_system.build_target.build_target_cls
import build_system.compiler.installed_instance


def setup_host_compiler_target_build_dir(root_dir: Path,
                                         host_compiler: build_system.compiler.installed_instance.CompilerInstance,
                                         target_build_dir: build_system.build_target.build_target_cls.BuildTarget):
    # TODO : WIP
    meson_launcher: str = _fetch_meson_launcher()

    cli_kwarg_assignment_op: Final[str] = r'='

    meson_cli_arg_setup_cmd: Final[str] = r'setup'
    meson_cli_arg_help: Final[str] = r'--help'
    meson_cli_arg_build_type: Final[str] = r'-buildtype' + cli_kwarg_assignment_op + target_build_dir.get_build_type().value
    meson_cli_arg_build_dir: Final[str] = str(target_build_dir.dir)
    meson_cli_arg_source_dir: Final[str] = str(root_dir)

    meson_cli_args: list[str] = [meson_cli_arg_setup_cmd,
                                 meson_cli_arg_build_type,
                                 meson_cli_arg_build_dir,
                                 meson_cli_arg_source_dir]

    try:
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
