# Generated by Django 3.0.1 on 2020-03-05 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_auto_20200305_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartproducts',
            name='imagePath',
            field=models.CharField(default=None, max_length=300),
        ),
    ]
