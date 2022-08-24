from sqlmodel import  create_engine, SQLModel, Session

from settings import settings

import os

engine = create_engine(
    url=settings.pg_dsn, 
    echo=settings.pg_echo, 
    future=settings.pg_future)

def init_db():
    if os.environ.get('SETTINGS_MODULE') == 'test':
        SQLModel.metadata.drop_all(engine)
        SQLModel.metadata.create_all(engine)
        
    
def get_session():
    with Session(engine) as session:
        yield session