from django.db import models


class Book(models.Model):
    title = models.CharField(verbose_name="Название", max_length=80)
    author = models.CharField(verbose_name="Автор", max_length=80)
    year = models.PositiveSmallIntegerField(verbose_name="Год издания")
    isbn = models.CharField(verbose_name="ISBN", max_length=13)
