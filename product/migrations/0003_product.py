# Generated by Django 3.0.1 on 2020-03-01 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('product_name', models.CharField(default=None, max_length=100)),
                ('category', models.CharField(default=None, max_length=50)),
                ('sub_catagory', models.CharField(default=None, max_length=50)),
                ('stock', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0.0)),
                ('img1', models.ImageField(default='product.jpg', upload_to='product_pics')),
                ('img2', models.ImageField(default='product.jpg', upload_to='product_pics')),
                ('img3', models.ImageField(default='product.jpg', upload_to='product_pics')),
                ('img4', models.ImageField(default='product.jpg', upload_to='product_pics')),
                ('img5', models.ImageField(default='product.jpg', upload_to='product_pics')),
            ],
        ),
    ]
