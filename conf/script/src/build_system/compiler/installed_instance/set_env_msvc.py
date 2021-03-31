import contextlib


class EnvMSVC(contextlib.AbstractContextManager):
    import build_system.compiler.installed_instance.msvc

    compiler: build_system.compiler.installed_instance.msvc.MSVCCompilerInstance

    def __init__(self, compiler: build_system.compiler.installed_instance.msvc.MSVCCompilerInstance) -> None:
        super().__init__()
        self.compiler = compiler

    def __enter__(self):
        self.__setup_env_vars()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.__teardown_env_vars()
        return False

    def __setup_env_vars(self) -> None:
        ...

    def __teardown_env_vars(self) -> None:
        ...
