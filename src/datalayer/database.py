from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from config import app_config

try:
    engine = create_async_engine(
        f"postgresql+asyncpg://{app_config.postgres.user}:{app_config.postgres.password}@{app_config.postgres.host}:{app_config.postgres.port}/{app_config.postgres.database}",
        pool_pre_ping=True,
        pool_recycle=1800,
        pool_size=30,
        echo=False,
    )
except Exception as e:
    print(f"Error loading config: {e}")
    exit(1)

# Database setup
AsyncSessionLocal = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# Dependency for getting DB session
async def get_db_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception as e:
            await session.rollback()
            print(f"Error committing session: {e}")
            raise
        finally:
            await session.close()
