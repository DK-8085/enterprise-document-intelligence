from app.core.config import Settings

def test_validate_default_settings():
    settings = Settings(env_file=None)
    assert settings.environment == "Development"
    assert settings.debug is True

def test_validate_with_custom_settings():
    settings = Settings(
        env_file=None,
        app_name="Test application",
        environment="Testing",
        debug=False
    )
    assert settings.app_name == "Test application"
    assert settings.environment == "Testing"
    assert settings.debug is False
