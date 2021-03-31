from configparser import ConfigParser
from dataclasses import dataclass
from pathlib import Path
from typing import Final

import build_system.compiler.family
import build_system.compiler.host.os_family
import build_system.compiler.reqs.scheme
import build_system.compiler.version


@dataclass(frozen=True)
class CompilerReqs:
    compiler_family: build_system.compiler.family.CompilerFamily
    os_families: list[build_system.compiler.host.os_family.OSFamily]
    min_compiler_version: build_system.compiler.version.CompilerVersion

    @staticmethod
    def get_default_compiler_reqs_file_path() -> Path:
        default_compiler_reqs_filename: Final[Path] = Path('compiler-reqs.ini')
        package_dir = Path(__file__).parent

        default_compiler_reqs_file = package_dir / default_compiler_reqs_filename
        default_compiler_reqs_file.resolve(strict=True)

        return default_compiler_reqs_file

    @classmethod
    def create_all_from_config_file(cls, file_path: Path = None) -> dict[build_system.compiler.family.CompilerFamily, 'CompilerReqs']:
        file_path = cls._check_file_path_for_default_param(file_path)
        cls.assure_file_path_integrity(file_path)

        config = ConfigParser(converters=cls._get_config_parser_converters())
        config.read(file_path)

        filtered_section_options_pairs = cls._filter_config_default_section(config)
        all_compilers_reqs = {}

        for compiler_name, compiler_reqs_section in filtered_section_options_pairs:
            # noinspection PyArgumentList
            compiler_family = build_system.compiler.family.CompilerFamily(compiler_name)
            os_families = compiler_reqs_section.getosfamily(build_system.compiler.reqs.scheme.CompilerReqsScheme.OS.value)
            min_compiler_version = cls.__read_min_version_from_config_compiler_reqs_section(compiler_reqs_section)

            compiler_reqs = cls(compiler_family=compiler_family, os_families=os_families, min_compiler_version=min_compiler_version)
            all_compilers_reqs[compiler_family] = compiler_reqs

        return all_compilers_reqs

    @staticmethod
    def __read_min_version_from_config_compiler_reqs_section(config_compiler_reqs_section) -> build_system.compiler.version.CompilerVersion:
        major = config_compiler_reqs_section.getint(build_system.compiler.reqs.scheme.CompilerReqsScheme.MAJOR.value)
        minor = config_compiler_reqs_section.getint(build_system.compiler.reqs.scheme.CompilerReqsScheme.MINOR.value, fallback=0)

        return build_system.compiler.version.CompilerVersion(major, minor)

    @classmethod
    def filter_by_os(cls,
                     all_compilers_reqs: dict[build_system.compiler.family.CompilerFamily, 'CompilerReqs'],
                     os_family: build_system.compiler.host.os_family.OSFamily) -> list['CompilerReqs']:
        return [compiler_reqs for compiler_family, compiler_reqs in all_compilers_reqs.items() if os_family in compiler_reqs.os_families]

    @classmethod
    def _check_file_path_for_default_param(cls, file_path: Path) -> Path:
        return file_path if file_path is not None else cls.get_default_compiler_reqs_file_path()

    @classmethod
    def _get_config_parser_converters(cls):
        return cls._get_config_parser_list_converter() | cls._get_config_parser_os_family_converter()

    # From https://stackoverflow.com/a/53274707/2924010
    @staticmethod
    def _get_config_parser_list_converter():
        return {'list': lambda whole_option: [split_options.strip() for split_options in whole_option.split(',')]}

    # From https://stackoverflow.com/a/53274707/2924010
    @staticmethod
    def _get_config_parser_os_family_converter():
        # noinspection PyArgumentList
        return {'osfamily': lambda whole_option: [build_system.compiler.host.os_family.OSFamily(split_options.strip()) for split_options in whole_option.split(',')]}

    @staticmethod
    def _filter_config_default_section(config: ConfigParser):
        return list(config.items())[1:]

    @staticmethod
    def assure_file_path_integrity(file_path: Path):
        if not file_path.exists() or not file_path.is_file():
            if file_path.is_dir():
                raise IsADirectoryError()
            raise FileNotFoundError()
