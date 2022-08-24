from fastapi import status, HTTPException, Depends
from fastapi.routing import APIRouter
from sqlmodel import Session
from sqlalchemy import exc as sa_exc

import schemas, models
from database.core import get_session
from .utils.user import create_user, get_current_active_user, get_user


router = APIRouter(
    prefix='/users',
    tags=['users']
)

@router.post('/create_user', status_code=status.HTTP_201_CREATED, response_model=schemas.User) 
def create_user_endpoint(request: schemas.UserPrivate, session: Session = Depends(get_session)) -> schemas.User:
    try:
        user = create_user(request, session)
    except sa_exc.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='This user already exists!')
    
    return schemas.User(name=user.name)

@router.get('/me', status_code=status.HTTP_200_OK, response_model=schemas.User)
def read_users_me(current_user: schemas.User = Depends(get_current_active_user)) -> schemas.User:
    return current_user

@router.get('/{username}', status_code=status.HTTP_200_OK, response_model=schemas.User)
def get_user_endpoint(username: str, session: Session = Depends(get_session)) -> schemas.User:
    user = get_user(username=username, session=session)
    if not user:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'User with name {username} does not exist'
            )
    return user