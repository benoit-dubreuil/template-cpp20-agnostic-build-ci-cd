class CompilerVersion:
    def __init__(self, major: int, minor: int = 0):
        self.major = major
        self.minor = minor

    def __str__(self) -> str:
        return '%u.%u' % (self.major, self.minor)
