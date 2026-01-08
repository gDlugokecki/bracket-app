from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)

    secret_key: str
    database_url: str


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
