from pydantic import BaseModel

class AccessToken(BaseModel):
    access_token: str 
    token_type: str
    
    @property
    def token(self):
        return self.access_token
    
class TokenData(BaseModel):
    username: str | None = None