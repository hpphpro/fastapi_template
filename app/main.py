from fastapi import FastAPI
import uvicorn

from routers import router
from database.core import init_db
from models.user import User 

app = FastAPI()

@app.on_event('startup')
def on_startup():
    init_db()
    
app.include_router(router)



if __name__ == '__main__':
    uvicorn.run('main:app', port=8001, reload=True)