# Generated by Django 3.2.3 on 2021-05-28 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_alter_book_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='text',
            field=models.TextField(default='a'),
            preserve_default=False,
        ),
    ]
