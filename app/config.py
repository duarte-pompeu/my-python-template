from __future__ import annotations

from pydantic import BaseSettings

# this uses the prebound method pattern
# further reading: https://python-patterns.guide/python/prebound-methods/
settings: Settings | None = None


class Settings(BaseSettings):
    example: str


def setup():
    global settings
    settings = Settings()
