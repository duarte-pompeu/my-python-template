from pydantic import BaseSettings

general: "GeneralSettings"


def setup():
    global general
    general = GeneralSettings()  # pyright: ignore


class GeneralSettings(BaseSettings):
    example: str
