from django.contrib import admin

from books.models import Book


@admin.register(Book)
class TaxationSystemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author', 'publication_date', 'type']
    search_fields = ['name', 'author']
    list_filter = ['type']
    ordering = ['name', 'author', 'publication_date']
