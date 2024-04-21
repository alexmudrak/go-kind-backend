from fastapi import APIRouter, Body, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies import bearer_token, get_session
from controllers.link_controllers import LinkController
from models.token_model import TokenModel
from schemas.link_schemas import LinkData

router = APIRouter()


@router.get("/")
async def get_links(
    token: TokenModel = Depends(bearer_token),
):
    pass


@router.post("/", response_model=LinkData)
async def create_link(
    link_data: LinkData = Body(...),
    token: TokenModel = Depends(bearer_token),
    db_session: AsyncSession = Depends(get_session),
):
    link_controller = LinkController(db_session, token)

    return await link_controller.create_link(link_data)
