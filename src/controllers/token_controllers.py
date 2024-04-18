from sqlalchemy.ext.asyncio import AsyncSession

from db.repositories.token_repository import TokenRepository
from models.token_model import TokenModel
from schemas.token_schemas import TokenData


class TokenController:
    def __init__(self, session: AsyncSession):
        self.token_resository = TokenRepository(session)

    async def create_or_update(
        self, user_id: int, data: dict
    ) -> TokenModel:
        token_data = TokenData.model_validate(
            data
        )
        token  = await self.token_resository.create_or_update(user_id, token_data)

        return token
