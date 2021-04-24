__all__ = ['CompilerVersion']

from dataclasses import dataclass


@dataclass(order=True, frozen=True)
class CompilerVersion:
    major: int
    minor: int = 0

    def __str__(self) -> str:
        return '%u%s%u' % (self.major, self.get_separator(), self.minor)

    # Ex: '9.1.9' => CompilerVersion(9, 1). The string must be stripped.
    @classmethod
    def create_from_str(cls, version_str: str) -> 'CompilerVersion':
        version_split: list[str] = version_str.split(cls.get_separator(), cls.get_dimension_count())

        if len(version_split) == 0 or (len(version_split) == 1 and not version_split[0]):
            raise ValueError('The supplied compiler version string is empty')

        try:
            major = int(version_split[cls.get_dimension_of_major()])
            minor = int(version_split[cls.get_dimension_of_minor()])
        except ValueError as raised_error:
            raise type(raised_error)('Cannot convert the supplied compiler version to integers').with_traceback(raised_error.__traceback__)

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
