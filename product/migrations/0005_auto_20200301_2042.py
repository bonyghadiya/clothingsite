# Generated by Django 3.0.1 on 2020-03-01 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_product_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='catagory',
        ),
    ]
