# Generated by Django 3.2.3 on 2021-05-28 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0003_book_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
