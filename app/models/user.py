from .base import BaseModel
from .base import Field
from pydantic import EmailStr

class User(BaseModel, table=True):
    __tablename__ = 'users'
    
    name: str = Field(
        sa_column_kwargs=dict(
            unique=True, 
            index=True,
            )
    ) 
    email: EmailStr = Field(
        default=None, 
        nullable=False,
    )
    password: str = Field(
        default=None,
        nullable=False,
    )