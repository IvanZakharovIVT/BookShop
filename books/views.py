import csv

from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action

from books.models import Book
from books.serializers.book import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=False, url_name='get_csv', url_path='get_csv')
    def get_csv(self, request, *args, **kwargs):
        book_list = super().list(request, *args, **kwargs)

        fieldnames = BookSerializer.Meta.fields

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export.csv"'

        writer = csv.writer(response)

        writer.writerow(fieldnames)

        for book in book_list.data:
            writer.writerow(book.values())

        return response
