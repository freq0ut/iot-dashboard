from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db

# ✅ Dependency to inject a database session
async def get_db_dependency() -> AsyncSession:
    db = await get_db().__anext__()  # Grab the next item from the async generator
    try:
        yield db
    finally:
        await db.close()
