import uuid

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from models.association import link_clicks
from models.link_model import LinkModel
from models.user_model import UserModel
from schemas.link_schemas import LinkData


class LinkRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_links(self, user_id: uuid.UUID) -> list[LinkModel]:
        async with self.session.begin():
            stmt = select(LinkModel).where(LinkModel.user_id == user_id)
            result = await self.session.execute(stmt)
            data = result.scalars().all()

            return list(data)

    async def create_link(
        self, user_id: uuid.UUID, link_data: LinkData
    ) -> LinkModel:
        async with self.session.begin():
            link = LinkModel(user_id=user_id, **link_data.model_dump())
            self.session.add(link)

            return link

    async def record_click(
        self, link_id: uuid.UUID, user_id: uuid.UUID
    ) -> None:
        async with self.session.begin():
            link_stmt = select(LinkModel).where(LinkModel.id == link_id)
            result = await self.session.execute(link_stmt)
            link = result.scalar_one_or_none()

            user_stmt = select(UserModel).where(UserModel.id == user_id)
            result = await self.session.execute(user_stmt)
            user = result.scalar_one_or_none()

            if link and user:
                click_exists_stmt = select(link_clicks).where(
                    (link_clicks.c.user_id == user_id)
                    & (link_clicks.c.link_id == link_id)
                )
                result = await self.session.execute(click_exists_stmt)
                click_exists = result.scalar_one_or_none()

                if not click_exists:
                    click = link_clicks.insert().values(
                        user_id=user_id, link_id=link_id
                    )
                    await self.session.execute(click)

    async def get_click_count(self, link_id: uuid.UUID) -> int:
        async with self.session.begin():
            stmt = (
                select(func.count())
                .select_from(link_clicks)
                .where(link_clicks.c.link_id == link_id)
            )
            result = await self.session.execute(stmt)
            count = result.scalar_one()

            return count

    async def get_user_click_count(
        self, link_id: uuid.UUID, user_id: uuid.UUID
    ) -> int:
        async with self.session.begin():
            stmt = (
                select(func.count())
                .select_from(link_clicks)
                .where(link_clicks.c.link_id == link_id)
                .where(link_clicks.c.user_id == user_id)
            )
            result = await self.session.execute(stmt)
            count = result.scalar_one()

            return count
