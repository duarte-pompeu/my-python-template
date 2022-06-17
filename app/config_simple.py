"""
Module where you can access your configurations.

It does the job, so feel free to use it.

But it's a bit more painful for testing.
Meaning, settings are automatically loaded at import time,
and other uses of the code such as testing will also need
to set up environment variables.

This is avoided in config_advanced.py.
"""
from pydantic import BaseSettings


class Settings(BaseSettings):
    example: str


settings = Settings()
