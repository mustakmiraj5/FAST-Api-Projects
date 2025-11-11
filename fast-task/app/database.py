from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base

# 1. Database URL for SQLite (async)
DATABASE_URL = "sqlite+aiosqlite:///./fasttask.db"

# 2. Create the async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# 3. Create session maker for async DB sessions
SessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

# 4. Base class for ORM models
Base = declarative_base()

# 5. Function to initialize the database (create tables)
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
