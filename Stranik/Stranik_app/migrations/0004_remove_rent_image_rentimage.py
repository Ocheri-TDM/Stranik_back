# Generated by Django 5.1.3 on 2025-03-19 16:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stranik_app', '0003_rent_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rent',
            name='image',
        ),
        migrations.CreateModel(
            name='RentImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos', verbose_name='Фотография')),
                ('is_main', models.BooleanField(default=False, verbose_name='Главное фото')),
                ('rent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Stranik_app.rent')),
            ],
            options={
                'verbose_name': 'Фотография локации',
                'verbose_name_plural': 'Фотографии локации',
            },
        ),
    ]
