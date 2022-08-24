from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    pg_dsn: PostgresDsn
    pg_echo: bool = False 
    pg_future: bool = True 
    secret_key: str 
    algorithm: str = 'HS256'
    access_token_expire_minutes: int = 30
    
    def __init__(self, module: BaseSettings = None, *args, **kwargs):
        super(Settings, self).__init__(*args, **kwargs)
        
        if module:
            self.__dict__.update(**module().__dict__)