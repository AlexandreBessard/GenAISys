from pydantic_settings import BaseSettings
"""
Class that helps you load configuration from a ".env" file.
"""
class Settings(BaseSettings):
    OPENAI_API_KEY: str | None = None

    class Config:
        env_file = ".env" # look for a file named '.env' in the project root.
        env_file_encoding = "utf-8"

settings = Settings()