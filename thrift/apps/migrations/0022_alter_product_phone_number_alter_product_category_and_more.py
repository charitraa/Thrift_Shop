# Generated by Django 5.0.1 on 2024-03-31 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0021_remove_product_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Phone_Number',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
