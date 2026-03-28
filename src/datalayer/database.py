from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlmodel import SQLModel
from config import app_config

# Import all models to ensure they are registered with SQLModel.metadata
from datalayer.model.db.auth import Auth

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

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

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
