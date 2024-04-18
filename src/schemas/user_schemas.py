from datetime import datetime

from pydantic import BaseModel


class UserData(BaseModel):
    twitter_id: int
    username: str
    nickname: str
