from sqlalchemy import Boolean, DateTime, Integer
from sqlalchemy.orm import declarative_base, mapped_column
from sqlalchemy.sql import func

Base = declarative_base()


class BaseAppModel(Base):
    __abstract__ = True

    id = mapped_column(
        Integer, primary_key=True, autoincrement=True, index=True
    )
    created = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated = mapped_column(
        DateTime(timezone=True), default=func.now(), onupdate=func.now()
    )
    deleted = mapped_column(Boolean, default=False)
