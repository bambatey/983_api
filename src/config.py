from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class PostgresSettings(BaseSettings):
    host: str = "localhost"
    port: int = 5432
    user: str = "postgres"
    password: str = "password"
    database: str = "database_name"

class AppConfig(BaseSettings):
    postgres: PostgresSettings = PostgresSettings()
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        case_sensitive=False,
        extra="ignore"
    )

app_config = AppConfig()
