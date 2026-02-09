from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from fastapi import HTTPException, status as s

from schemas.books import SBook, SBookAdd
from models.books import BooksModel

class BooksRepository:
    
    @classmethod
    async def add_book(
        cls,
        data: SBookAdd,
        session: AsyncSession,
    ) -> BooksModel:
        
        book = BooksModel(**data.model_dump())

        session.add(book)
        await session.commit()
        await session.refresh(book)

        return book
    
    @classmethod
    async def get_all_books(cls, session: AsyncSession):

        query = select(BooksModel)
        result = await session.execute(query)

        return result.scalars().all()
    
    @classmethod
    async def get_book(
        cls,
        id: int,
        session: AsyncSession,
    ) -> BooksModel:
        
        query = (select(BooksModel)
                 .where(BooksModel.id == id)
                )
        result = await session.execute(query)
        book = result.scalars().one_or_none()

        if book is None:
            raise HTTPException(
                status_code=s.HTTP_404_NOT_FOUND,
                detail='Книга не найдена'
            )
        
        return book
    
    @classmethod
    async def update_book(
        cls,
        id: int,
        book: SBookAdd,
        session: AsyncSession,
    ) -> BooksModel:
        
        obj = await cls.get_book(id, session) # 404 если нет
        data = book.model_dump()

        for k,v in data.items():
            setattr(obj, k, v)

        await session.commit()
        await session.refresh(obj)
        
        return obj
    
    @classmethod
    async def delete_book(
        cls,
        id: int,
        session: AsyncSession
    ):
        obj = await cls.get_book(id, session)  # 404 если нет
        await session.delete(obj)
        await session.commit()
