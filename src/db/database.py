from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from core.config import settings

DATABASE_URL = settings.db_url

# TODO: echo state should be linked to APP_MODE
engine = create_async_engine(
    DATABASE_URL, echo=False, pool_size=10, max_overflow=20
)

AsyncSessionFactory = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

