from django.db import models
from datetime import datetime

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)


class Bookshop(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100,blank=True)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    genre = models.CharField(max_length=50, blank=True)
    author = models.CharField(max_length=100, blank=True)
    year = models.CharField(max_length=50, blank=True)
    date = models.DateTimeField(default=datetime.now())
    is_favorite = models.BooleanField(default=False)
