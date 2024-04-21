from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies import bearer_token
from controllers.user_controllers import UserController
from db.session import get_session
from models.token_model import TokenModel
from schemas.user_schemas import UserData

router = APIRouter()


@router.get("/me", response_model=UserData)
async def get_me(
    token: TokenModel = Depends(bearer_token),
    db_session: AsyncSession = Depends(get_session)
):
    user_controller = UserController(db_session)

    return await user_controller.get_user_by_id(token.user_id)
