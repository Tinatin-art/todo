from django.db import models

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)


class BookShop(models.Model):
    text = models.CharField(max_length=140)
    subtitle = models.CharField(max_length=140)
    description = models.CharField(max_length=140)
    genres = models.CharField(max_length=140)
    year = models.DateField(default=0)
    