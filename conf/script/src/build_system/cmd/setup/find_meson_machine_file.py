from pathlib import Path
from typing import Final

import build_system.build_target.build_target
import build_system.compiler.installed_instance


def _find_native_machine_files_dir(meson_machine_files_dir: Path) -> Path:
    native_dir_name: Final[str] = r'native'
    native_machine_files_dir = _find_machine_files_dir(parent_machine_files_dir=meson_machine_files_dir, machine_files_dir_name=native_dir_name)

    return native_machine_files_dir


def _find_compiler_machine_file(native_machine_files_dir: Path,
                                compiler_instance: build_system.compiler.installed_instance.CompilerInstance) -> Path:
    compiler_machine_files_dir_name: Final[str] = r'compiler'
    compiler_machine_file_name: str = compiler_instance.compiler_family.value

    compiler_machine_file = _find_machine_file(parent_machine_files_dir=native_machine_files_dir,
                                               machine_files_dir_name=compiler_machine_files_dir_name,
                                               machine_file_name=compiler_machine_file_name)

    return compiler_machine_file


def _find_build_type_machine_file(native_machine_files_dir: Path,
                                  build_target: build_system.build_target.build_target.BuildTarget) -> Path:
    build_type_machine_files_dir_name: Final[str] = r'build_type'
    build_type_file_name: str = build_target.target_build_type.value

    build_type_file = _find_machine_file(parent_machine_files_dir=native_machine_files_dir,
                                         machine_files_dir_name=build_type_machine_files_dir_name,
                                         machine_file_name=build_type_file_name)

    return build_type_file


def _find_sanitizer_machine_file(native_machine_files_dir: Path,
                                 build_target: build_system.build_target.build_target.BuildTarget) -> Path:
    sanitizer_machine_files_dir_name: Final[str] = r'sanitizer'
    sanitizer_file_name: str = build_target.sanitizer.value

    sanitizer_file = _find_machine_file(parent_machine_files_dir=native_machine_files_dir,
                                        machine_files_dir_name=sanitizer_machine_files_dir_name,
                                        machine_file_name=sanitizer_file_name)

    return sanitizer_file


def _find_machine_files_dir(parent_machine_files_dir: Path, machine_files_dir_name: str) -> Path:
    machine_files_dir: Path = parent_machine_files_dir / machine_files_dir_name
    machine_files_dir.resolve(strict=True)
    machine_files_dir = machine_files_dir.absolute()

    return machine_files_dir


def _find_machine_file(parent_machine_files_dir: Path, machine_files_dir_name: str, machine_file_name: str) -> Path:
    extension: Final[str] = r'.ini'

    machine_files_dir: Path = _find_machine_files_dir(parent_machine_files_dir=parent_machine_files_dir, machine_files_dir_name=machine_files_dir_name)

    machine_file: Path = machine_files_dir / machine_file_name
    machine_file = machine_file.with_suffix(extension)
    machine_file.resolve(strict=True)

    return machine_file
