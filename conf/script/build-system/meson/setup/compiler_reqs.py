from pathlib import Path
from configparser import ConfigParser

from auto_print import auto_repr, auto_str
from compiler_version import CompilerVersion
from data_model import Compiler, OSFamily, CompilerReqsSectionScheme


@auto_repr
@auto_str
class CompilerReqs:
    def __init__(self, compiler: Compiler, os_families: list[OSFamily], version: CompilerVersion):
        self.compiler = compiler
        self.os_families = os_families
        self.version = version

    @staticmethod
    def get_default_compiler_reqs_file_path() -> Path:
        return Path('compiler-reqs.ini')

    @classmethod
    def create_all_from_file(cls, file_path: Path = None) -> dict[Compiler, 'CompilerReqs']:
        file_path = cls._check_file_path_for_default_param(file_path)
        cls._assure_file_path_integrity(file_path)

        config = ConfigParser(converters=cls._get_config_parser_converters())
        config.read(file_path)

        filtered_section_options_pairs = cls._filter_config_default_section(config)
        all_compilers_reqs = {}

        for compiler_name, compiler_reqs_section in filtered_section_options_pairs:
            compiler = Compiler(compiler_name)
            os_families = compiler_reqs_section.getosfamily(CompilerReqsSectionScheme.OS.value)
            compiler_version = CompilerVersion.create_from_config_compiler_reqs_section(compiler_reqs_section)

            compiler_reqs = cls(compiler, os_families, compiler_version)
            all_compilers_reqs[compiler] = compiler_reqs

        return all_compilers_reqs

    @classmethod
    def filter_by_os(cls, all_compilers_reqs: dict[Compiler, 'CompilerReqs'], os_family: OSFamily) -> list['CompilerReqs']:
        return [compiler_reqs for compiler, compiler_reqs in all_compilers_reqs.items() if os_family in compiler_reqs.os_families]

    @classmethod
    def _check_file_path_for_default_param(cls, file_path: Path) -> Path:
        return file_path if file_path is not None else cls.get_default_compiler_reqs_file_path()

    @staticmethod
    def _assure_file_path_integrity(file_path: Path):
        if not file_path.exists() or not file_path.is_file():
            if file_path.is_dir():
                raise IsADirectoryError()
            raise FileNotFoundError()

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
        return {'osfamily': lambda whole_option: [OSFamily(split_options.strip()) for split_options in whole_option.split(',')]}

    @staticmethod
    def _filter_config_default_section(config: ConfigParser):
        return list(config.items())[1:]
