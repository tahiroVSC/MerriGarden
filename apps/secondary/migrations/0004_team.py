# Generated by Django 5.0 on 2023-12-26 04:40

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0003_usluga_alter_condition_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя_боса')),
                ('image_boss', models.ImageField(upload_to='image_boss/', verbose_name='Фото боса')),
                ('about_boss', ckeditor.fields.RichTextField(verbose_name='Информация про боса')),
                ('image', models.ImageField(upload_to='image_team/', verbose_name='Фото мемберов')),
                ('team_name', models.CharField(max_length=255, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Команда',
                'verbose_name_plural': 'Команды',
            },
        ),
    ]
