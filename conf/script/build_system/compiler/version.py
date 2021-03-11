from build_system.compiler.reqs.scheme import CompilerReqsScheme
from utils.auto_print import auto_repr


@auto_repr
class CompilerVersion:
    def __init__(self, major: int, minor: int = 0):
        self.major = major
        self.minor = minor

    def __str__(self) -> str:
        return '%u%s%u' % (self.major, self.get_separator(), self.minor)

    @classmethod
    def create_from_config_compiler_reqs_section(cls, config_compiler_reqs_section) -> 'CompilerVersion':
        major = config_compiler_reqs_section.getint(CompilerReqsScheme.MAJOR.value)
        minor = config_compiler_reqs_section.getint(CompilerReqsScheme.MINOR.value, fallback=0)

        return cls(major, minor)

    # Ex: '9.1.9' => CompilerVersion(9, 1). The string must be stripped.
    @classmethod
    def create_from_str(cls, version_str: str) -> 'CompilerVersion':
        version_split: list[str] = version_str.split(cls.get_separator(), cls.get_dimension_count())

        if len(version_split) == 0 or (len(version_split) == 1 and not version_split[0]):
            raise ValueError('The supplied compiler version string is empty')

        try:
            major = int(version_split[cls.get_dimension_of_major()])
            minor = int(version_split[cls.get_dimension_of_minor()])
        except ValueError as raised_exception:
            raise type(raised_exception)('Cannot convert the supplied compiler version to integers').with_traceback(raised_exception.__traceback__)

        return CompilerVersion(major, minor)

    @staticmethod
    def get_dimension_of_major() -> int:
        return 0

    @classmethod
    def get_dimension_of_minor(cls) -> int:
        return cls.get_dimension_of_major() + 1

    @staticmethod
    def get_dimension_count() -> int:
        """Gets the numbers of dimensions represented by the :class:`~CompilerVersion` data model, i.e. :var:`~CompilerVersion.major`.:var:`~CompilerVersion.minor` => 2
        dimensions

        The dimensions count can be used as the `maxsplit` argument in the :func:`~str.split` method.
        """
        return 2

    @staticmethod
    def get_separator() -> str:
        """Gets the separator used to represent as a string :class:`~CompilerVersion`s data model

        Example
        =======
        `9.2.0` where `.` is the separator
        """
        return '.'
