from rest_framework import viewsets

from books.models import Book
from books.serializers.book import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    model = Book
    serializer_class = BookSerializer
