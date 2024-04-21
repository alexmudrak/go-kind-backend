import uuid
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base_model import BaseAppModel


class LinkModel(BaseAppModel):
    __tablename__ = "links"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))

    user = relationship("UserModel", back_populates="links")
