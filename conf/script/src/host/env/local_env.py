__all__ = ['LocalEnv']

from dataclasses import dataclass

from .env_var import *


@dataclass(init=False, order=True)
class LocalEnv:
    env_vars: list[EnvVar]
