import uuid
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from db.repositories.link_repository import LinkRepository
from models.token_model import TokenModel
from schemas.link_schemas import LinkData, ReadLinkData


class LinkController:
    def __init__(self, session: AsyncSession, token: TokenModel):
        self.link_resository = LinkRepository(session)
        self.user = token.user

    async def get_links(self) -> list[ReadLinkData]:
        return [
            ReadLinkData.model_validate(link)
            for link in await self.link_resository.get_links(self.user.id)
        ]

    async def create_link(self, link_data: LinkData) -> ReadLinkData:
        try:
            link = await self.link_resository.create_link(
                self.user.id, link_data
            )
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="A link with the same user_id, name, beneficiary, and description already exists.",
            )

        return ReadLinkData.model_validate(link)
    
    async def record_click(self, link_id: uuid.UUID):
        await self.link_resository.record_click(link_id, self.user.id)

        return await self.link_resository.get_user_click_count(link_id, self.user.id)
