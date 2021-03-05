#!/usr/bin/env python3

from typing import Final
from pathlib import Path
from configparser import ConfigParser
from data_model import Compiler, OSFamily, CompilerReqsSectionScheme


class CompilerVersion:
    def __init__(self, major: int, minor: int = 0):
        self.major = major
        self.minor = minor

    def __str__(self) -> str:
        return '%u.%u' % (self.major, self.minor)


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

        config = ConfigParser(converters=cls._get_config_parser_list_converter())
        config.read(file_path)
        filtered_section_options_pairs = cls._filter_config_default_section(config)

        for compiler_name, raw_compiler_reqs in filtered_section_options_pairs:
            # Transform raw_compiler_reqs into treated reqs
            #   OS
            #   Version
            # Put all results inside dictionary to return

            compiler = Compiler(compiler_name)

            raw_os = raw_compiler_reqs.getlist(CompilerReqsSectionScheme.OS.value)
            raw_major = raw_compiler_reqs.getint(CompilerReqsSectionScheme.MAJOR.value)
            raw_minor = raw_compiler_reqs.getint(CompilerReqsSectionScheme.MINOR.value)

        return {}  # TODO

    @classmethod
    def _check_file_path_for_default_param(cls, file_path: Path) -> Path:
        return file_path if file_path is not None else cls.get_default_compiler_reqs_file_path()

    @staticmethod
    def _assure_file_path_integrity(file_path: Path):
        if not file_path.exists() or not file_path.is_file():
            if file_path.is_dir():
                raise IsADirectoryError()
            raise FileNotFoundError()

    # From https://stackoverflow.com/a/53274707/2924010
    @staticmethod
    def _get_config_parser_list_converter():
        return {'list': lambda x: [i.strip() for i in x.split(',')]}

    @staticmethod
    def _filter_config_default_section(config: ConfigParser):
        return list(config.items())[1:]

    #    @classmethod
    #    def create_tmp_instance(cls, config: ConfigParser, compiler: Compiler):
    #        option_minor: Final = CompilerRequirementsSectionScheme.MINOR.value
    #        section = config[compiler.value]
    #        assert section is not None
    #
    #        # TODO : https://stackoverflow.com/a/53274707/2924010
    #        all_os = section.getlist(CompilerRequirementsSectionScheme.OS.value, fallback=None)
    #        assert all_os is not None
    #        os_families = [OSFamily.enum_members[os.lower()] for os in all_os]
    #
    #        major = section.getint(CompilerRequirementsSectionScheme.MAJOR.value, fallback=None)
    #        assert major is not None
    #
    #        if config.has_option(section.name, option_minor):
    #            minor = section.getint(option_minor, fallback=None)
    #            assert minor is not None
    #            version = CompilerVersion(major, minor)
    #        else:
    #            version = CompilerVersion(major)
    #
    #        return CompilerRequirements(compiler, os_families, version)


CompilerReqs.create_all_from_file()

# COMPILER_REQ_FILE: Final = 'compiler-reqs.ini'
#
# config = ConfigParser()
# config.read(COMPILER_REQ_FILE)
#
# compiler_reqs = CompilerRequirements.create(config, Compiler.MSVC)
# print(compiler_reqs)
#
# filtered_items = filter_config_default_section(config)
#
# for section, items in filtered_items:
#     print('Section:', section)
#     print('Items:')
#
#     for key, value in items.items():
#         print(key, value, sep=' = ')
#     print()
