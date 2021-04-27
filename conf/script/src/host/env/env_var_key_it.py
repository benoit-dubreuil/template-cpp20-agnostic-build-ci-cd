__all__ = ['EnvVarKeyIt']

from typing import final

from .env_var_base_it import *
from .env_var_fwd import *


@final
class EnvVarKeyIt(EnvVarBaseIt[T_Key]):

    def _peek_next(self) -> T_Key:
        return self.get_env_var().get_env_key()
