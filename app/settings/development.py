from pydantic import BaseSettings

class Settings(BaseSettings):
    pg_echo: bool = True
    
    class Config:
        env_file = '.env/development'