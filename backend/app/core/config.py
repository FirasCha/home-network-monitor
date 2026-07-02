from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str
    app_version: str

    api_host: str
    api_port: int

    mongo_host: str
    mongo_port: int
    mongo_database: str

    mongo_username: str = ""
    mongo_password: str = ""

    log_level: str

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
