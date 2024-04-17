from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column

from models.base_model import BaseAppModel


class UserModel(BaseAppModel):
    __tablename__ = "users"

    twitter_id = mapped_column(Integer, nullable=False)
    username = mapped_column(String, nullable=True)
    nickname = mapped_column(String, nullable=True)
