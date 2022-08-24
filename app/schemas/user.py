from pydantic import BaseModel, EmailStr 

class User(BaseModel):
    name: str 

class UserPrivate(User):
    email: EmailStr
    password: str 
    confirm_password: str 
  