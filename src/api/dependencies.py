import datetime
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession


from db.repositories.token_repository import TokenRepository
from db.session import get_session
from models.token_model import TokenModel

async def bearer_token(
    credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
    db_session: AsyncSession = Depends(get_session)
) -> TokenModel:
    token_repository = TokenRepository(db_session)
    token = await token_repository.get_token_by_access_token(credentials.credentials)
    if not token or token.access_token_expire < datetime.datetime.now(datetime.timezone.utc):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )
    return token
