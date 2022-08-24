from sqlmodel import Session
from fastapi import status, HTTPException, Depends
from jose import JWTError, jwt

import schemas, models
from .auth.password import compare_password, get_password_hash, verify_password
from .auth.token import ALGORITHM, SECRET_KEY, oauth_scheme
from database.core import get_session

def create_user(user: schemas.UserPrivate, session: Session = Depends()) -> models.User:
    if not compare_password(user.password, user.confirm_password):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
            detail='Passwords are not equal'
        )
    password = get_password_hash(user.password)
    user = models.User(
        name=user.name,
        email=user.email,
        password=password
        )
    session.add(user)
    session.commit()
    session.refresh(user)
    
    return user

def get_user(username: str, session: Session = Depends()) -> models.User:
    user = session.query(models.User).filter(models.User.name==username).first()
    if not user:
        return False
    
    return user

def get_current_user(token: str = Depends(oauth_scheme), session: Session = Depends(get_session)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username=token_data.username, session=session)
    if not user:
        raise credentials_exception
    
    return user

def get_current_active_user(current_user: schemas.User = Depends(get_current_user)):
    return current_user

def authenticate_user(username: str, password: str, session: Session):
    user = get_user(username=username, session=session)
    if not user or not verify_password(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user