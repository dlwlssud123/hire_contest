from typing import List, Union
from pydantic import AnyHttpUrl, validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "CareerPath AI"
    ENV: str = "development"
    API_V1_STR: str = "/api/v1"
    
    # CORS
    BACKEND_CORS_ORIGINS: List[Union[str, AnyHttpUrl]] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]

    # Database & Redis
    DATABASE_URL: str = "postgresql+asyncpg://careerpath:careerpath_secret@localhost:5432/careerpath_db"
    REDIS_URL: str = "redis://localhost:6379/0"

    # AI & LLM
    OPENAI_API_KEY: str = ""
    ANTHROPIC_API_KEY: str = ""
    DEFAULT_LLM_MODEL: str = "gpt-4o"

    # Public Data APIs
    EMPLOYMENT24_API_KEY: str = ""
    QNET_API_KEY: str = ""
    PUBLIC_DATA_PORTAL_KEY: str = ""

    # Security
    SECRET_KEY: str = "careerpath-secret-super-key-change-in-production"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
