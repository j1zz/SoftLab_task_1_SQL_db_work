# Generated by Django 3.2.9 on 2021-11-26 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors_books', '0002_rename_books_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='id',
        ),
        migrations.RemoveField(
            model_name='book',
            name='title',
        ),
        migrations.AddField(
            model_name='book',
            name='author_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
