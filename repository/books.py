from sqlalchemy.ext.asyncio import AsyncSession

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
    

