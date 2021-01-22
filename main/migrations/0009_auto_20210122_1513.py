# Generated by Django 3.1.4 on 2021-01-22 09:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210122_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookshop',
            name='author',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='bookshop',
            name='genre',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='bookshop',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 22, 15, 13, 3, 279625)),
        ),
    ]
