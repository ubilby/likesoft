# Generated by Django 4.2.7 on 2023-11-25 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Account',
            new_name='User',
        ),
    ]
