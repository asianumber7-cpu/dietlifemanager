import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Diet Life Manager"
    API_V1_STR: str = "/api/v1"
    
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "user")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "password")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "db")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "diet_db")
    
    # --- [IBM Watson 설정 추가] ---
    IBM_CLOUD_URL: str = os.getenv("IBM_CLOUD_URL", "")
    IBM_API_KEY: str = os.getenv("IBM_API_KEY", "")
    IBM_PROJECT_ID: str = os.getenv("IBM_PROJECT_ID", "")
    # ---------------------------

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}/{self.POSTGRES_DB}"

settings = Settings()