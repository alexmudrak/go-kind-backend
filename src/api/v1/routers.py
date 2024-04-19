from fastapi import APIRouter

from api.v1.endpoints import twitter
from api.v1.endpoints import user

router = APIRouter()

router.include_router(twitter.router, tags=["Twitter"], prefix="/twitter")
router.include_router(user.router, tags=["User"], prefix="/user")

