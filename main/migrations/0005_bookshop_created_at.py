# Generated by Django 3.1.4 on 2021-01-22 08:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_bookshop'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookshop',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 22, 14, 34, 21, 499291)),
        ),
    ]
