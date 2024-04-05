from fastapi import APIRouter, HTTPException, Request
from starlette import status
from starlette.responses import RedirectResponse

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
    authorize_url = twitter.get_authorization_url()
    return RedirectResponse(url=authorize_url)


@router.get(
    "/authorize",
    response_model=TwitterAccessTokenResponse,
)
async def authorize_twitter(request: Request):
    query_params = dict(request.query_params)

    if "code" not in query_params or "state" not in query_params:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Missing 'code' or 'state' query parameters.",
        )
    url = str(request.url)
    access_token = twitter.get_access_token(url)

    return access_token
