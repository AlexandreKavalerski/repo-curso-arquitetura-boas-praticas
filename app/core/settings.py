from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./soccer.db"
    APP_NAME: str = "Soccer Manager"
    DEBUG: bool = False


settings = Settings()
