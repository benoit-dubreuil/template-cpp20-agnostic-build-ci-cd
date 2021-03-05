from data_model import CompilerReqsSectionScheme


class CompilerVersion:
    def __init__(self, major: int, minor: int = 0):
        self.major = major
        self.minor = minor

    def __str__(self) -> str:
        return '%u.%u' % (self.major, self.minor)

    def __repr__(self) -> str:
        return 'CompilerVersion(%s)' % str(self)

    @classmethod
    def create_from_config_compiler_reqs_section(cls, config_compiler_reqs_section) -> 'CompilerVersion':
        major = config_compiler_reqs_section.getint(CompilerReqsSectionScheme.MAJOR.value)
        minor = config_compiler_reqs_section.getint(CompilerReqsSectionScheme.MINOR.value, fallback=0)

        return cls(major, minor)
