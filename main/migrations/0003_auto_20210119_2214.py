# Generated by Django 3.1.4 on 2021-01-19 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_bookshop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookshop',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='bookshop',
            name='is_closed',
        ),
        migrations.RemoveField(
            model_name='bookshop',
            name='is_favorite',
        ),
        migrations.AddField(
            model_name='bookshop',
            name='description',
            field=models.CharField(default='SOME STRING', max_length=140),
        ),
        migrations.AddField(
            model_name='bookshop',
            name='genres',
            field=models.CharField(default='SOME STRING', max_length=140),
        ),
        migrations.AddField(
            model_name='bookshop',
            name='price',
            field=models.PositiveIntegerField(default='SOME NUMBER'),
        ),
        migrations.AddField(
            model_name='bookshop',
            name='subtitle',
            field=models.CharField(default='SOME STRING', max_length=140),
        ),
        migrations.AddField(
            model_name='bookshop',
            name='year',
            field=models.DateField(auto_created=True, null=True),
        ),
        migrations.AlterField(
            model_name='bookshop',
            name='text',
            field=models.CharField(default='SOME STRING', max_length=140),
        ),
    ]