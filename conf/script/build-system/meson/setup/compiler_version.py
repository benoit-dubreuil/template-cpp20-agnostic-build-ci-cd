from auto_print import auto_repr
from data_model import CompilerReqsSectionScheme


@auto_repr
class CompilerVersion:
    def __init__(self, major: int, minor: int = 0):
        self.major = major
        self.minor = minor

    def __str__(self) -> str:
        return '%u%s%u' % (self.major, self.get_separator(), self.minor)

    @classmethod
    def create_from_config_compiler_reqs_section(cls, config_compiler_reqs_section) -> 'CompilerVersion':
        major = config_compiler_reqs_section.getint(CompilerReqsSectionScheme.MAJOR.value)
        minor = config_compiler_reqs_section.getint(CompilerReqsSectionScheme.MINOR.value, fallback=0)

        return cls(major, minor)

    @staticmethod
    def get_dimension_count() -> int:
        """Gets the numbers of dimensions represented by the :class:`~CompilerVersion` data model, i.e. :var:`~CompilerVersion.major`.:var:`~CompilerVersion.minor` => 2
        dimensions"""
        return 2

    @staticmethod
    def get_separator() -> str:
        """Gets the separator used to represent as a string :class:`~CompilerVersion`s data model

        Example
        =======
        `9.2.0` where `.` is the separator
        """
        return '.'
