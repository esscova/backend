from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from typing import ClassVar

class Settings(BaseSettings):
    API_V1_STR:str = '/api/v1'
    DB_URL:str = 'sqlite+aiosqlite:///database.db'
    DBBaseModel:ClassVar = declarative_base()

    JWT_SECRET:str ='Py7pmQk597pGYm2NaDfX_v8NIrb9T1d9zKZ8xkYCtqo' # gerado pela lib secrets
    """
    import secrets
    secrets.token_urlsafe(32)
    """
    ALGORITHM:str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES:int = 60 * 24 * 7 # token para uma semana

    class Config:
        case_sensitive = True

settings:Settings = Settings()