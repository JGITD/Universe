# Generated by Django 4.1.1 on 2022-09-30 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universe_app', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='/media/default/profile2.jpg', upload_to='profile_pics'),
        ),
    ]
