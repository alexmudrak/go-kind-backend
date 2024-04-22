from sqlalchemy import (
    UUID,
    Column,
    DateTime,
    ForeignKey,
    Table,
    UniqueConstraint,
    func,
)

from models.base_model import Base

link_clicks = Table(
    "link_clicks",
    Base.metadata,
    Column("created", DateTime(timezone=True), server_default=func.now()),
    Column("user_id", UUID(as_uuid=True), ForeignKey("users.id")),
    Column("link_id", UUID(as_uuid=True), ForeignKey("links.id")),
    UniqueConstraint("user_id", "link_id", name="uix_user_link"),
)
