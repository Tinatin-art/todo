# Generated by Django 3.1.4 on 2021-01-19 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210119_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookshop',
            name='price',
            field=models.IntegerField(),
        ),
    ]