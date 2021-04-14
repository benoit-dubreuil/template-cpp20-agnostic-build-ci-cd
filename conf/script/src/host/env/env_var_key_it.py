import typing

import host.env.env_var_base_it
import host.env.env_var_fwd as _fwd


@typing.final
class EnvVarKeyIt(host.env.env_var_base_it.EnvVarBaseIt[_fwd.T_Key]):

    def _peek_next(self) -> _fwd.T_Key:
        return self.get_env_var().get_env_key()
