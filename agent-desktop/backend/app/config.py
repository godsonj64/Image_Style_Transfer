from functools import lru_cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Local-First Agent Desktop Backend"
    app_version: str = "0.2.0"
    environment: str = Field(default="dev")
    data_dir: Path = Field(default=Path("data"))
    sqlite_filename: str = Field(default="app.db")

    model_config = SettingsConfigDict(env_prefix="AGENT_DESKTOP_", env_file=".env", extra="ignore")

    @property
    def sqlite_path(self) -> Path:
        return self.data_dir / self.sqlite_filename


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    settings = Settings()
    settings.data_dir.mkdir(parents=True, exist_ok=True)
    return settings
