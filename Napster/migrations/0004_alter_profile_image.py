# Generated by Django 4.0.4 on 2022-04-20 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Napster', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='media/default.jpg', upload_to='profile_pic'),
        ),
    ]