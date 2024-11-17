from django.db import models

from books.enums.book_type import BookGenre
from books.models.base_model import BaseModel


class Book(BaseModel):
    """Книги"""
    BOOK_TYPES = tuple(
        ((book_type.value, book_type.description) for book_type in BookGenre)
    )
    name = models.CharField(max_length=50, verbose_name='Название')
    author = models.CharField(max_length=50, verbose_name='Автор')
    publication_date = models.DateField(verbose_name='Дата публикации')
    type = models.CharField(choices=BOOK_TYPES, max_length=30, verbose_name='Жанр книги')

    class Meta:
        verbose_name = "Книги"
