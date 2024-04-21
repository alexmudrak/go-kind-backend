from fastapi import APIRouter, Depends

from api.dependencies import bearer_token
from models.token_model import TokenModel
from schemas.user_schemas import UserData

router = APIRouter()


@router.get("/me", response_model=UserData)
async def get_me(
    token: TokenModel = Depends(bearer_token),
):
    return UserData(
        twitter_id=token.user.twitter_id,
        username=token.user.username,
        nickname=token.user.nickname,
    )
