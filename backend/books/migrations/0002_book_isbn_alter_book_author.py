# Generated by Django 4.2.7 on 2023-11-22 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.CharField(default=0, max_length=13, verbose_name='ISBN'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=80, verbose_name='Автор'),
        ),
    ]
