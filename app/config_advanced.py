"""
Module where you can access your configurations, with delayed loading.

There's a simpler version in config_simple.py.
"""


from __future__ import annotations

from pydantic import BaseSettings

settings: Settings


class Settings(BaseSettings):
    example: str


def __getattr__(name):
    global _settings

    # this will setup necessary config when someone tries to get the settings
    # it's useful to delay this, so we don't need to apply configurations at import time
    # eg tests may import modules without loading configuration from .env
    if name == "settings":
        if not _settings:
            _settings = Settings()

        return _settings
    else:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")


_settings: Settings | None = None
