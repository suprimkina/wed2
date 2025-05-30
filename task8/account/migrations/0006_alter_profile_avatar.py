# Generated by Django 5.1 on 2024-10-11 06:10

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/', validators=[account.models.image_size_validator, account.models.image_resolution_validator, account.models.image_aspect_ratio_validator]),
        ),
    ]
