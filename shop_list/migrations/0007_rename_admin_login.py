# Generated by Django 4.2.1 on 2023-10-10 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_list', '0006_admin'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Admin',
            new_name='Login',
        ),
    ]