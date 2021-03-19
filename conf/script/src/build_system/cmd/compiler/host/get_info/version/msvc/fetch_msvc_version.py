from pathlib import Path
from typing import Final, Optional

import vswhere

from build_system.compiler.version import CompilerVersion

_PROP_VERSION: Final[str] = 'installationVersion'


def fetch(compiler_installation_path: Optional[Path] = None) -> Optional[CompilerVersion]:
    interpreted_compiler_version: Optional[CompilerVersion] = None
    compiler_installation_path = build_system.cmd.compiler.host.get_info.location.msvc.installation_path.find(compiler_installation_path)

    if compiler_installation_path is not None:
        fetched_compiler_version: Optional[str] = vswhere.find_first(prop=_PROP_VERSION, path=compiler_installation_path)

        if fetched_compiler_version is not None:
            fetched_compiler_version = fetched_compiler_version.strip()
            interpreted_compiler_version = CompilerVersion.create_from_str(fetched_compiler_version)

    return interpreted_compiler_version
