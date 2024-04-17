from sqlalchemy.ext.asyncio import AsyncSession

from db.repositories.user_repository import UserRepository
from models.user_model import UserModel
from schemas.user_schemas import UserData


class UserController:
    def __init__(self, session: AsyncSession):
        self.user_resository = UserRepository(session)

    async def get_or_create(
        self, user_id: int, user_name: str, user_username: str
    ) -> UserModel:
        user_data = UserData(
            twitter_id=user_id,
            username=user_name,
            nickname=user_username,
        )
        user, status = await self.user_resository.get_or_create(user_data)

        return user
