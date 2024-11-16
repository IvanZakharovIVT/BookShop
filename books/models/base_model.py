from django.db import models


class BaseModel(models.Model):
    """Абстрактная модель для отслеживания времени создания и изменения объекта"""
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_modified = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        abstract = True
