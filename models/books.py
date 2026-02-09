from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import CheckConstraint, Index
from database import Model

class BooksModel(Model):
    __tablename__ = 'books'
    
    id: Mapped[int] = mapped_column(
        primary_key=True,
        init=False, # т.к. Model наследуется от MappedAsDataclass 
    )
    title: Mapped[str] = mapped_column(
        nullable=False,
    )
    author: Mapped[str] = mapped_column(
        nullable=False,
    )
    year: Mapped[int | None] = mapped_column(
        nullable=True,
    )
    pages: Mapped[int | None] = mapped_column(
        nullable=True,
    )
    is_read: Mapped[bool] = mapped_column(
        default=False,
        server_default='false', # на случай если создается не через ORM
        nullable=False,
    )
    

    __table_args__ = (
        # Ограничение на релевантный год и положительное количество страниц
        CheckConstraint(
            '(year IS NULL) OR (year BETWEEN -2000 AND 2100)',
            name='ck_books_year_range',
        ),
        CheckConstraint(
            '(pages IS NULL) OR (pages > 10)',
            name='ck_pages_positive',
        ),
        # Индексы под частые запросы
        Index('ix_books_author',  'author'),
        Index('ix_books_is_read', 'is_read'),
    )