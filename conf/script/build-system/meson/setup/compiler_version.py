from auto_print import auto_repr
from data_model import CompilerReqsSectionScheme


@auto_repr
class CompilerVersion:
    def __init__(self, major: int, minor: int = 0):
        self.major = major
        self.minor = minor

    def __str__(self) -> str:
        return '%u.%u' % (self.major, self.minor)

    @classmethod
    def create_from_config_compiler_reqs_section(cls, config_compiler_reqs_section) -> 'CompilerVersion':
        major = config_compiler_reqs_section.getint(CompilerReqsSectionScheme.MAJOR.value)
        minor = config_compiler_reqs_section.getint(CompilerReqsSectionScheme.MINOR.value, fallback=0)

        return cls(major, minor)
