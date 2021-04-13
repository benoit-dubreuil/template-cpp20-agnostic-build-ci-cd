from dataclasses import dataclass

from host.env.env_var import EnvVar


@dataclass(init=False, order=True)
class LocalEnv:
    env_vars: list[EnvVar]
