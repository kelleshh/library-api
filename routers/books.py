from fastapi import (
    APIRouter,
    status as s,
)

from schemas.books import SBookAdd, SBook
from database import SessionDep
from repository.books import BooksRepository as BR

router = APIRouter(
    prefix='/books',
    tags=['Книги'],
)

@router.post('/', status_code=s.HTTP_201_CREATED)
async def add_book(
    book: SBookAdd,
    session: SessionDep,
) -> SBook:
    new_book = await BR.add_book(book, session)
    
    return new_book # type: ignore

@router.get('/', status_code=s.HTTP_200_OK)
async def get_all_books(session: SessionDep) -> list[SBook]:
    pass

@router.get('/{id}', status_code=s.HTTP_200_OK)
async def get_book(
    id: int,
    session: SessionDep,
) -> SBook:
    pass

@router.put('/{id}', status_code=s.HTTP_200_OK)
async def update_book(
    id: int,
    book: SBookAdd,
    session: SessionDep,
) -> SBook:
    pass

@router.delete('/{id}', status_code=s.HTTP_204_NO_CONTENT)
async def delete_book(
    id: int,
    session: SessionDep,
) -> None:
    pass