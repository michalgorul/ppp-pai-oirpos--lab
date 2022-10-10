from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    login: str = Field("admin")
    pswd: str = Field("admin")

    class Config:
        env_file = "ENV/local.env"
        env_file_encoding = "utf-8"


settings = Settings()
