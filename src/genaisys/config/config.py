from pathlib import Path
from pydantic_settings import BaseSettings

# Get the genaisys package directory (2 levels up from this file)
PACKAGE_ROOT = Path(__file__).resolve().parents[1]

"""
Class that helps you load configuration from a ".env" file.
"""
class Settings(BaseSettings):
    OPENAI_API_KEY: str | None = None
    PINECONE_API_KEY: str | None = None

    class Config:
        env_file = PACKAGE_ROOT / ".env"  # Absolute path to .env in src/genaisys/
        env_file_encoding = "utf-8"

settings = Settings()