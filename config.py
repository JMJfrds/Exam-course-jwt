from pydantic_settings import BaseSettings
from functools import lru_cache


class ConfigSettings(BaseSettings):

    db_user: str
    db_password: int
    db_host: str
    db_port: int
    db_name: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "allow"

@lru_cache
def get_settings():
    return ConfigSettings()


class AuthConf(BaseSettings):
    secret_key: str
    algorithm: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "allow"


@lru_cache
def get_auth():
    return AuthConf()