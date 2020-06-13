# Generated by Django 2.2.7 on 2020-06-13 06:17

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], default='male', max_length=20)),
                ('email', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=150)),
                ('status', models.CharField(choices=[('active', 'Active'), ('archived', 'Archived'), ('deleted', 'Deleted')], default='active', max_length=20)),
                ('username', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
