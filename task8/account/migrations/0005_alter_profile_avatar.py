# Generated by Django 5.1 on 2024-10-09 09:57

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_profile_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/', validators=[account.models.image_size_validator, account.models.image_resolution_validator]),
        ),
    ]
