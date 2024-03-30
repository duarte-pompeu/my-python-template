# TODO(cookiecutter): use pydantic_settings instead of pydantic
from pydantic_settings import BaseSettings


general: "GeneralSettings"


def setup():
    global general
    general = GeneralSettings()  # pyright: ignore


class GeneralSettings(BaseSettings):
    example: str
