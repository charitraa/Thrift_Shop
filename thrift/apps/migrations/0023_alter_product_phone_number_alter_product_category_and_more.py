# Generated by Django 5.0.1 on 2024-03-31 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0022_alter_product_phone_number_alter_product_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Phone_Number',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
        migrations.DeleteModel(
            name='cart',
        ),
    ]
