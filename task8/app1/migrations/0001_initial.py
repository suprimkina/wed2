# Generated by Django 5.1 on 2024-09-27 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProgLang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prog_lang_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=255)),
                ('bday', models.DateField()),
                ('sex', models.CharField(max_length=5)),
                ('biography', models.TextField(blank=True, max_length=512, null=True)),
                ('prog_langs', models.ManyToManyField(to='app1.proglang')),
            ],
        ),
    ]
