# Generated by Django 5.0.6 on 2024-05-25 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CTF_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar_images/'),
        ),
    ]
