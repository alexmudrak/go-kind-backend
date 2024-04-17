from db.database import AsyncSessionFactory


async def get_session():
    async with AsyncSessionFactory() as session:
        try:
            yield session
        except:
            await session.rollback()
            raise
        finally:
            await session.close()

