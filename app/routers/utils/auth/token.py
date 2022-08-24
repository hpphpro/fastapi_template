from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

from datetime import timedelta, datetime

from settings import settings


SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm

oauth_scheme = OAuth2PasswordBearer(tokenUrl='login')

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({
        'exp': expire
    })
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt