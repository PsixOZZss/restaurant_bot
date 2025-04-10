from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: str
    DATABASE_NAME: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
BOT_TOKEN = settings.BOT_TOKEN
DATABASE_NAME = settings.DATABASE_NAME
