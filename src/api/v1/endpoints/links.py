import uuid

from fastapi import APIRouter, Body, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies import bearer_token, get_session
from controllers.link_controllers import LinkController
from models.token_model import TokenModel
from schemas.link_schemas import LinkData, ReadLinkData

router = APIRouter()


@router.get("/", response_model=list[ReadLinkData])
async def get_links(
    token: TokenModel = Depends(bearer_token),
    db_session: AsyncSession = Depends(get_session),
):
    link_controller = LinkController(db_session, token)

    return await link_controller.get_links()


@router.post("/", response_model=ReadLinkData)
async def create_link(
    link_data: LinkData = Body(...),
    token: TokenModel = Depends(bearer_token),
    db_session: AsyncSession = Depends(get_session),
):
    link_controller = LinkController(db_session, token)

    return await link_controller.create_link(link_data)


@router.get("/click/{link_id}")
async def click_link(
    link_id: uuid.UUID,
    token: TokenModel = Depends(bearer_token),
    db_session: AsyncSession = Depends(get_session),
):
    link_controller = LinkController(db_session, token)

    return await link_controller.record_click(link_id)
