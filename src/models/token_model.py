from datetime import datetime
import uuid
from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base_model import BaseAppModel


class TokenModel(BaseAppModel):
    __tablename__ = "tokens"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    access_token: Mapped[str] = mapped_column(nullable=False)
    access_token_expire: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    refresh_token: Mapped[str] =  mapped_column(nullable=False)

    user = relationship("UserModel", back_populates="token")
