# Generated by Django 3.1.4 on 2021-01-22 09:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210122_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookshop',
            name='created_at',
        ),
        migrations.AddField(
            model_name='bookshop',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 22, 15, 21, 11, 281640)),
        ),
        migrations.AddField(
            model_name='bookshop',
            name='year',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]