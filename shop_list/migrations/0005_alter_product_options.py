# Generated by Django 4.2.1 on 2023-10-09 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_list', '0004_catalog_section_name_ru_product_name_ru_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name', 'counting', 'name_unit')},
        ),
    ]
