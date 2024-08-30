# Generated by Django 5.0.1 on 2024-03-24 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_alter_customer_email_alter_customer_gender_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(max_length=200)),
                ('Product_Price', models.IntegerField()),
                ('Description', models.TextField()),
                ('Location', models.TextField()),
                ('Phone_Number', models.IntegerField()),
            ],
        ),
    ]