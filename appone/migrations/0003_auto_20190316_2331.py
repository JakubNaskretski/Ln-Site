# Generated by Django 2.1.7 on 2019-03-16 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0002_auto_20190316_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(upload_to='static/product_photo'),
        ),
    ]
