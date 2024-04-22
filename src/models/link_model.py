import uuid

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base_model import BaseAppModel
from models.association import link_clicks


class LinkModel(BaseAppModel):
    __tablename__ = "links"
    __table_args__ = (
        UniqueConstraint(
            "user_id", "name", "beneficiary", "description", name="uix_1"
        ),
    )

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    name: Mapped[str] = mapped_column(nullable=True, default="")
    beneficiary: Mapped[str] = mapped_column(nullable=True, default="")
    description: Mapped[str] = mapped_column(nullable=True, default="")
    
    clickers = relationship(
        "UserModel",
        secondary=link_clicks,
        back_populates="clicked_links",
    )
    user = relationship("UserModel", back_populates="links")
