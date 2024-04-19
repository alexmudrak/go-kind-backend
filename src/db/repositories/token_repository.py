from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from models.token_model import TokenModel
from schemas.token_schemas import TokenData


class TokenRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_token_by_access_token(self, access_token: str) -> TokenModel:
        query = (
            select(TokenModel)
            .where(TokenModel.access_token == access_token)
        )
        result = await self.session.execute(query)

        return result.scalars().first()

    async def create_or_update(self, user_id: int, token_data: TokenData) -> TokenModel:
        async with self.session.begin():
            query = select(TokenModel).where(TokenModel.user_id == user_id)

            result = await self.session.execute(query)
            token = result.scalars().first()

            token_expire = datetime.fromtimestamp(token_data.expires_at)

            if token is None:
                token = TokenModel(
                    user_id=user_id,
                    access_token=token_data.access_token,
                    access_token_expire=token_expire,
                    refresh_token=token_data.refresh_token,
                )
                self.session.add(token)
            else:
                token.access_token = token_data.access_token
                token.access_token_expire = token_expire
                token.refresh_token = token_data.refresh_token

            await self.session.flush()

            return token
