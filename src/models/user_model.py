from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base_model import BaseAppModel
from models.association import link_clicks

class UserModel(BaseAppModel):
    __tablename__ = "users"

    twitter_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    username: Mapped[str] = mapped_column(nullable=True)
    nickname: Mapped[str] = mapped_column(nullable=True)

    clicked_links = relationship(
        "LinkModel",
        secondary=link_clicks,
        back_populates="clickers",
    )
    token = relationship("TokenModel", uselist=False, back_populates="user")
    links = relationship("LinkModel", back_populates="user")
