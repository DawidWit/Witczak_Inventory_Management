from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    PROJECT_NAME: str = "Inventory Platform"
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:3000"]
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    ALLOWED_ORIGINS: List[str] = ["*"]  # or read from env

    class Config:
        case_sensitive = True

settings = Settings()
