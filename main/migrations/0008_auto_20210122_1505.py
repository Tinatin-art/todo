# Generated by Django 3.1.4 on 2021-01-22 09:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210122_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookshop',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bookshop',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 22, 15, 5, 56, 391367)),
        ),
    ]
