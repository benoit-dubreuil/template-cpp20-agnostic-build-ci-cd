from pathlib import Path

import mesonbuild.mesonmain

import build_system.build_target.build_target_cls
import build_system.compiler.installed_instance


def setup_host_compiler_target_build_dir(root_dir: Path,
                                         host_compiler: build_system.compiler.installed_instance.CompilerInstance,
                                         target_build_dir: build_system.build_target.build_target_cls.BuildTarget):
    # TODO : WIP
    meson_launcher: str = _fetch_meson_launcher()
    meson_cli_args: list[str] = ['-h']

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
