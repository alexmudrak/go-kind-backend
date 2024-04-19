from sqlalchemy.ext.asyncio import AsyncSession

from db.repositories.user_repository import UserRepository
from models.user_model import UserModel
from schemas.user_schemas import UserData


class UserController:
    def __init__(self, session: AsyncSession):
        self.user_resository = UserRepository(session)

    async def get_user_by_id(self, user_id: int) -> UserData:
        user = await self.user_resository.get_user_by_id(user_id)

        return UserData(
            twitter_id=user.twitter_id,
            username=user.username,
            nickname=user.nickname,
        )

    async def get_or_create(
        self, user_twitter_id: int, user_name: str, user_username: str
    ) -> UserModel:
        user_data = UserData(
            twitter_id=user_twitter_id,
            username=user_name,
            nickname=user_username,
        )
        user, status = await self.user_resository.get_or_create(user_data)

        return user
