from django.db import models

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)


class BookShop(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    subtitle = models.CharField("Подзаголовок", max_length=100)
    description = models.TextField("Описание")
    price = models.PositiveIntegerField("Цена")
    genres = models.CharField("Жанры", max_length=100)
    author = models.CharField("Имя", max_length=100)
    year = models.PositiveSmallIntegerField("Дата выхода", default=2020)
    date = models.DateField("Дата", auto_now_add=True)