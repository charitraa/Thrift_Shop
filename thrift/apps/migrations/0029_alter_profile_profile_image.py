# Generated by Django 5.0.1 on 2024-04-02 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0028_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='static/back.jpg', upload_to='profile'),
        ),
    ]