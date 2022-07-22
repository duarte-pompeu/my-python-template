"""
Tests settings from config_advanced.py.

Unlike config_simple, you may import the module without loading configuration.
"""

import pytest
from pydantic import ValidationError

from app.config import GeneralSettings


def test_empty_settings():
    """
    Tests that settings model cannot be empty.

    This test wouldn't be possible if we always loaded the configuration.
    But with the prebound method pattern, we can executing tests without configurations!
    """
    with pytest.raises(ValidationError):
        GeneralSettings()


def test_populated_settings():
    settings = GeneralSettings(example="hey")
    assert settings.example == "hey"
