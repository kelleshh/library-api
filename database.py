from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from typing import Annotated

DATABASE_URL = "sqlite+aiosqlite:////home/kelle/library-api/library.db"


engine = create_async_engine(DATABASE_URL)

new_session = async_sessionmaker(engine, expire_on_commit=False)

class Model(DeclarativeBase, MappedAsDataclass):
    pass

async def get_db():
    async with new_session() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_db)]