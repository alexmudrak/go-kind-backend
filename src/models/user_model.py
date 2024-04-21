from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base_model import BaseAppModel

class UserModel(BaseAppModel):
    __tablename__ = "users"

    twitter_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    username: Mapped[str] = mapped_column(nullable=True)
    nickname: Mapped[str] = mapped_column(nullable=True)

    token = relationship("TokenModel", uselist=False, back_populates="user")
    links = relationship("LinkModel", back_populates="user")
