from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, declarative_base, mapped_column
from sqlalchemy.sql import func

Base = declarative_base()


class BaseAppModel(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True, index=True
    )
    created: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=func.now(), onupdate=func.now()
    )
    deleted: Mapped[bool] = mapped_column(default=False)
