from datetime import datetime

from sqlalchemy import UUID, DateTime
from sqlalchemy.orm import Mapped, declarative_base, mapped_column
from sqlalchemy.sql import func
import uuid


Base = declarative_base()


class BaseAppModel(Base):
    __abstract__ = True

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True),
        primary_key=True, default=uuid.uuid4, index=True
    )
    created: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=func.now(), onupdate=func.now()
    )
    deleted: Mapped[bool] = mapped_column(default=False)
