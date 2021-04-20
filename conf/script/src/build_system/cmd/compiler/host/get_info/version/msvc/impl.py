from pathlib import Path
from typing import Final, Optional

import vswhere

import build_system.cmd.compiler.host.get_info.location.msvc
import build_system.compiler.core.version

_PROP_VERSION: Final[str] = 'installationVersion'


def fetch_msvc_version(compiler_installation_path: Optional[Path] = None) -> Optional[build_system.compiler.core.version.CompilerVersion]:
    interpreted_compiler_version: Optional[build_system.compiler.core.version.CompilerVersion] = None
    compiler_installation_path = build_system.cmd.compiler.host.get_info.location.msvc.find_msvc_location(compiler_installation_path)

    if compiler_installation_path is not None:
        fetched_compiler_version: Optional[str] = vswhere.find_first(prop=_PROP_VERSION, path=compiler_installation_path)

        if fetched_compiler_version is not None:
            fetched_compiler_version = fetched_compiler_version.strip()
            interpreted_compiler_version = build_system.compiler.core.version.CompilerVersion.create_from_str(fetched_compiler_version)

    return interpreted_compiler_version
