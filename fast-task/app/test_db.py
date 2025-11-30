import asyncio
from sqlalchemy import text
from app.database import engine

async def check_db():
    async with engine.connect() as conn:
        result = await conn.execute(
            text("SELECT name FROM sqlite_master WHERE type='table'")
        )
        tables = [row[0] for row in result.fetchall()]
        print("Tables in the database:", tables)

asyncio.run(check_db())
