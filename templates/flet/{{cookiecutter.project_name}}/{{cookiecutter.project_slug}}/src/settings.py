from functools import lru_cache
from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import SettingsConfigDict
from pydantic_settings_yaml import YamlBaseSettings


class DatabaseSettings(BaseModel):
    user: str
    password: str
    host: str
    port: int
    db: str


class AppSettings(YamlBaseSettings):
    model_config = SettingsConfigDict(yaml_file=Path(__file__).parent.parent.parent / "settings.yml")
    database: DatabaseSettings


@lru_cache
def get_app_settings():
    return AppSettings()
