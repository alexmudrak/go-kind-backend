from fastapi import APIRouter

from api.v1.endpoints import twitter
from api.v1.endpoints import users
from api.v1.endpoints import links

router = APIRouter()

router.include_router(twitter.router, tags=["Twitter"], prefix="/twitter")
router.include_router(users.router, tags=["Users"], prefix="/users")
router.include_router(links.router, tags=["Links"], prefix="/links")

