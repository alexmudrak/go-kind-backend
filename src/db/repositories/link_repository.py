import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from models.link_model import LinkModel
from schemas.link_schemas import LinkData


class LinkRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_links(self):
        pass

    async def create_link(
        self, user_id: uuid.UUID, link_data: LinkData
    ) -> LinkModel:
        async with self.session.begin():
            link = LinkModel(user_id=user_id, **link_data.model_dump())
            self.session.add(link)

            return link
