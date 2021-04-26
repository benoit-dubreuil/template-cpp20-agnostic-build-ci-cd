__all__ = ['generate_meson_machine_files_args']

from pathlib import Path
from typing import Final

from build_system.build_target import *
from build_system.cmd.hierarchy import *
from build_system.compiler import *
from .find_meson_machine_file import *


def generate_meson_machine_files_args(compiler_instance: CompilerInstance,
                                      build_target: BuildTarget) -> list[str]:
    meson_machine_files_dir = find_meson_machine_files_dir()
    native_machine_files_dir = find_native_machine_files_dir(meson_machine_files_dir=meson_machine_files_dir)

    machine_files = _assemble_machine_files(compiler_instance=compiler_instance,
                                            build_target=build_target,
                                            meson_machine_files_dir=meson_machine_files_dir,
                                            native_machine_files_dir=native_machine_files_dir)

    machine_files_args: list[str] = _machine_files_to_args(machine_files=machine_files)
    _insert_setup_arg_native_file(machine_files_args=machine_files_args)

    return machine_files_args


def _assemble_machine_files(compiler_instance: CompilerInstance,
                            build_target: BuildTarget,
                            meson_machine_files_dir: Path,
                            native_machine_files_dir: Path) -> list[Path]:
    return [meson_machine_files_dir / r'pre-global.ini',
            native_machine_files_dir / r'native.ini',
            find_compiler_machine_file(native_machine_files_dir=native_machine_files_dir, compiler_instance=compiler_instance),
            find_build_type_machine_file(native_machine_files_dir=native_machine_files_dir, build_target=build_target),
            find_sanitizer_machine_file(native_machine_files_dir=native_machine_files_dir, build_target=build_target),
            meson_machine_files_dir / r'post-global.ini']


def _machine_files_to_args(machine_files: list[Path]) -> list[str]:
    return [str(machine_file) for machine_file in machine_files]


def _insert_setup_arg_native_file(machine_files_args: list[str]) -> None:
    setup_arg_native_file: Final[str] = r'--native-file'
    step: Final[int] = 2

    for i in range(0, len(machine_files_args) * step, step):
        machine_files_args.insert(i, setup_arg_native_file)
