# Generated by Django 5.0.7 on 2024-07-28 11:43

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('completed', models.BooleanField(default=False, verbose_name='Выполнение')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
    ]
