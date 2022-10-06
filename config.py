from pydantic import BaseSettings


class Settings(BaseSettings):
    resource_path: str

    class Config:
        env_file = "../ENV/local.env"
        env_file_encoding = "utf-8"


settings = Settings()
