# Generated by Django 4.2.5 on 2023-09-05 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, upload_to='product_image'),
            preserve_default=False,
        ),
    ]
