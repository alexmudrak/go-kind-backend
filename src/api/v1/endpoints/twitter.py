from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.responses import RedirectResponse

from api.dependencies import get_session
from core.config import settings
from integrations.twitter_integrations import TwitterAuthenticator
from schemas.twitter_schemas import TwitterAccessTokenResponse

router = APIRouter()

twitter = TwitterAuthenticator(
    client_id=settings.app_client_id,
    client_secret=settings.app_client_secret,
    redirect_uri=settings.app_redirect_uri,
    scope=settings.app_scopes,
)


@router.get("/login")
async def login_twitter():
    authorize_url = await twitter.get_authorization_url()
    return RedirectResponse(url=authorize_url)


@router.get("/refresh/{refresh_token}")
async def refresh_twitter(
    refresh_token: str, db_session: AsyncSession = Depends(get_session)
):
    result = await twitter.refresh_user_token(refresh_token, db_session)

    return result


@router.get(
    "/authorize",
    response_model=TwitterAccessTokenResponse,
)
async def authorize_twitter(
    request: Request, db_session: AsyncSession = Depends(get_session)
):
    query_params = dict(request.query_params)

    if "code" not in query_params or "state" not in query_params:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Missing 'code' or 'state' query parameters.",
        )
    url = str(request.url)
    access_token = await twitter.get_access_token(url, db_session)

    return access_token
