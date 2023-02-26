from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_HOSTNAME: str

    BUS_USER: str
    BUS_PASSWORD: str
    BUS_HOSTNAME: str
    BUS_PORT: int

    class Config:
        env_file = './.env'


settings = Settings()