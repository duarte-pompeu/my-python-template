import pytest
from pydantic import ValidationError

from app.config import Settings


def test_empty_settings():
    """
    Tests that settings model cannot be empty.

    This test wouldn't be possible if we always loaded the configuration.
    But with the prebound method pattern, we can executing tests without configurations!
    """
    with pytest.raises(ValidationError):
        Settings()


def test_populated_settings():
    settings = Settings(example="hey")
    assert settings.example == "hey"
