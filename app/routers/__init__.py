from fastapi.routing import APIRouter

from . import user 
from . import login

router = APIRouter()

router.include_router(user.router)
router.include_router(login.router)
