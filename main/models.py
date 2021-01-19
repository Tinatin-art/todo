from django.db import models

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)


class BookShop(models.Model):
    text = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.PositiveIntegerField(max_length=50)
    genres = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.DateField(auto_created=True)