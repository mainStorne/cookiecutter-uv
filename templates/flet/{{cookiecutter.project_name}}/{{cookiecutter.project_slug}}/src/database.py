from functools import lru_cache

from pydantic import PostgresDsn
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession

from src.settings import DatabaseSettings, get_app_settings


class Database:
    def __init__(self, database_settings: DatabaseSettings):
        self._sqlalchemy_url = PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=database_settings.user,
            password=database_settings.password,
            host=database_settings.host,
            port=database_settings.port,
            path=database_settings.db,
        )

        self._engine = create_async_engine(str(self._sqlalchemy_url))
        self.session_maker = async_sessionmaker(self._engine, expire_on_commit=False, class_=AsyncSession)


@lru_cache
def get_database():
    app_settings = get_app_settings()
    return Database(app_settings.database)
