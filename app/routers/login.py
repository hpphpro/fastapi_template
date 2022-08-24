from fastapi import Depends, status, HTTPException
from fastapi.routing import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

from datetime import timedelta
from routers.utils.user import authenticate_user


import schemas, models
from database.core import get_session
from .utils.auth.token import create_access_token
from settings import settings


router = APIRouter(
    tags=['auth']
)

@router.post('/login', status_code=status.HTTP_202_ACCEPTED, response_model=schemas.AccessToken)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)) -> schemas.AccessToken:
    user = authenticate_user(username=form_data.username, password=form_data.password, session=session)
    
    acces_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={'sub': user.name},
        expires_delta=acces_token_expires
    )
    return {'access_token': access_token, 'token_type': 'bearer'}