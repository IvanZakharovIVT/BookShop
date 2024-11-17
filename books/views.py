import csv

from django.http import HttpResponse
from qs2csv import qs_to_csv
from rest_framework import viewsets
from rest_framework.decorators import action

from books.models import Book
from books.serializers.book import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=False, url_name='get_csv', url_path='get_csv')
    def get_csv(self, request, *args, **kwargs):
        l = super().list(request, *args, **kwargs)

        # Get the fieldnames from the serializer
        fieldnames = BookSerializer.Meta.fields

        # Create the CSV response
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export.csv"'

        # Write the header row
        writer = csv.writer(response, delimiter='\t', dialect='excel')

        writer.writerow(fieldnames)

        for e in l.data:
            writer.writerow([e[fieldname] for fieldname in fieldnames])

        return response
