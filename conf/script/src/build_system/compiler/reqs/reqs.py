from configparser import ConfigParser
from dataclasses import dataclass
from pathlib import Path
from typing import Final

import build_system.compiler.family
import build_system.compiler.reqs.scheme
import build_system.compiler.version
import host.os_family
import utils.error.cls_def
import utils.error.try_external_errors


@dataclass(frozen=True)
class CompilerReqs:
    compiler_family: build_system.compiler.family.CompilerFamily
    os_families: list[host.os_family.OSFamily]
    min_compiler_version: build_system.compiler.version.CompilerVersion

    @classmethod
    def get_defaul_config_file(cls) -> Path:
        import build_system.cmd.hierarchy.find_conf_dir

        default_config_filename: Final[Path] = Path('compiler-reqs.ini')
        conf_build_system_dir: Path = build_system.cmd.hierarchy.find_conf_dir.find_conf_build_system_dir()

        default_config_file = conf_build_system_dir / default_config_filename
        cls._assure_config_file_integrity(config_file=default_config_file)

        return default_config_file

    @classmethod
    def create_all_from_config_file(cls, config_file: Path = None) -> dict[build_system.compiler.family.CompilerFamily, 'CompilerReqs']:
        config_file = cls._check_config_file_for_default_param(config_file=config_file)
        cls._assure_config_file_integrity(config_file=config_file)

        config = ConfigParser(converters=cls._get_config_parser_converters())
        config.read(config_file)

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
                     os_family: host.os_family.OSFamily) -> list['CompilerReqs']:
        return [compiler_reqs for compiler_family, compiler_reqs in all_compilers_reqs.items() if os_family in compiler_reqs.os_families]

    @classmethod
    def _check_config_file_for_default_param(cls, config_file: Path) -> Path:
        return config_file if config_file is not None else cls.get_defaul_config_file()

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
        return {'osfamily': lambda whole_option: [host.os_family.OSFamily(split_options.strip()) for split_options in whole_option.split(',')]}

    @staticmethod
    def _filter_config_default_section(config: ConfigParser):
        return list(config.items())[1:]

    @staticmethod
    def _assure_config_file_integrity(config_file: Path):
        utils.error.try_external_errors.try_manage_strict_path_resolving(path_to_resolve=config_file,
                                                                         external_errors_to_manage={(Exception,): utils.error.cls_def.CompilerReqsNotFoundError})

        if config_file.is_dir():
            raise utils.error.cls_def.CompilerReqsNotFoundError()
