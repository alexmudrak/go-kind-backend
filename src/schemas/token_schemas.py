from pydantic import BaseModel


class TokenData(BaseModel):
    token_type: str
    expires_in: int
    access_token: str
    scope: list[str]
    refresh_token: str
    expires_at: float
