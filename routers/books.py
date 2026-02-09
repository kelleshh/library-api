from typing import Sequence

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

@router.post('/', status_code=s.HTTP_201_CREATED, response_model=SBook)
async def add_book(
    book: SBookAdd,
    session: SessionDep,
):
    new_book = await BR.add_book(book, session)
    
    return SBook.model_validate(new_book)


@router.get('/', status_code=s.HTTP_200_OK, response_model=list[SBook])
async def get_all_books(session: SessionDep):
    return await BR.get_all_books(session) 

@router.get('/{id}', status_code=s.HTTP_200_OK, response_model=SBook)
async def get_book(
    id: int,
    session: SessionDep,
):
    return await BR.get_book(id, session)
    
    

@router.put('/{id}', status_code=s.HTTP_200_OK, response_model=SBook)
async def update_book(
    id: int,
    book: SBookAdd,
    session: SessionDep,
):
    return await BR.update_book(id, book, session)


@router.delete('/{id}', status_code=s.HTTP_204_NO_CONTENT)
async def delete_book(
    id: int,
    session: SessionDep,
) -> None:
    await BR.delete_book(id, session)