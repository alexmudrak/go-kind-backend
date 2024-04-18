from datetime import datetime
from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base_model import BaseAppModel


class TokenModel(BaseAppModel):
    __tablename__ = "tokens"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    access_token: Mapped[str] = mapped_column(nullable=False)
    access_token_expire: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    reshresh_token: Mapped[str] =  mapped_column(nullable=False)
    refresh_token_expire: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    user = relationship("UserModel", back_populates="token")
