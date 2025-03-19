# Generated by Django 5.1.3 on 2025-03-04 11:39

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название категории')),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название локации')),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='Фотография')),
                ('cost_value', models.IntegerField(blank=True, default=0, null=True, verbose_name='Цена (числовое значение)')),
                ('pop', models.IntegerField(default=0, verbose_name='Популярность')),
                ('date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата публикации')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Stranik_app.category', verbose_name='Выберите категорию')),
            ],
            options={
                'verbose_name': 'Аренда',
                'verbose_name_plural': 'Аренда',
                'ordering': ['-date'],
            },
        ),
    ]
