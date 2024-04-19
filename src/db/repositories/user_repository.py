from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.user_model import UserModel
from schemas.user_schemas import UserData


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_user_by_id(self, user_id: int) -> UserModel:
        query = select(UserModel).where(
            UserModel.id == user_id
        )
        result = await self.session.execute(query)
        user = result.scalar_one_or_none()

        return user

    async def get_or_create(
        self, user_data: UserData
    ) -> tuple[UserModel, bool]:
        async with self.session.begin():
            query = select(UserModel).where(
                UserModel.twitter_id == user_data.twitter_id
            )
            result = await self.session.execute(query)
            user = result.scalar_one_or_none()

            if user:
                return user, False

            new_user = UserModel(**user_data.model_dump())
            self.session.add(new_user)
            await self.session.flush()

            return new_user, True
