# Generated by Django 5.0 on 2023-12-27 10:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0015_delete_blogdetail_news_descriptions1_news_letter'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='descriptions2',
            field=ckeditor.fields.RichTextField(default=1, verbose_name='Описание1'),
            preserve_default=False,
        ),
    ]
