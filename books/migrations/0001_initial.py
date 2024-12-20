# Generated by Django 5.1.3 on 2024-11-16 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('author', models.CharField(max_length=50, verbose_name='Автор')),
                ('publication_date', models.DateField(verbose_name='Дата публикации')),
                ('type', models.CharField(choices=[('Sci-fi', 'Научная фантастика'), ('fantasy', 'Фэнтези'), ('detective', 'Детектив'), ('comedy', 'Комедия'), ('drama', 'Драма')], max_length=30, verbose_name='Жанр книги')),
            ],
            options={
                'verbose_name': 'Книги',
            },
        ),
    ]
