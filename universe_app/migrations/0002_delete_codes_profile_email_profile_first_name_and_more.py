# Generated by Django 4.1.1 on 2022-09-30 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universe_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Codes',
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='verification_code',
            field=models.CharField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
