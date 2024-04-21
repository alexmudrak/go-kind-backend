from fastapi import APIRouter, Depends

from api.dependencies import bearer_token
from models.token_model import TokenModel

router = APIRouter()


@router.get("/")
async def get_links(
    token: TokenModel = Depends(bearer_token),
):
    pass


@router.post("/")
async def create_link(
    token: TokenModel = Depends(bearer_token),
):
    pass
