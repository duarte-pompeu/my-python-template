"""
Module where you can access your configurations, with delayed loading.

There's a simpler version in config_simple.py.
"""


from __future__ import annotations

from loguru import logger
from pydantic import BaseSettings

settings: Settings


class Settings(BaseSettings):
    example: str


def __getattr__(name):
    global _settings

    # this will setup necessary config if someone tries to get the settings
    # but hasn't set manually set up things
    # it's useful to delay this, so we don't need to apply configurations when not needed, eg unit tests
    if name == "settings":
        if not _settings:
            setup()

        return _settings
    else:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")


def setup():
    global _settings
    try:
        _settings = Settings()
    except Exception as e:
        logger.error(e)
        logger.error(
            "This may have been caused by an empty or invalid .env file. Please see example.env for examples."
        )
        raise
    logger.debug(
        f"Populed settings based on environment variables: {_settings.__dict__}"
    )


_settings: Settings | None = None
