from fastapi import APIRouter

from api.v1.endpoints import twitter

router = APIRouter()

router.include_router(twitter.router, tags=["Twitter"], prefix="/twitter")

