from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str= "Enterprise Document Intelligence"
    environment: str= "Development"
    debug: bool = True
    api_version: str = "v1"

    model_config=SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"

        )

@lru_cache
def get_settings()->Settings:
    return Settings()
