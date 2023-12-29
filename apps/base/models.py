from django.db import models
from ckeditor.fields import RichTextField
from django_resized.forms import ResizedImageField
# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = ' Название'
    )
    descriptions = RichTextField(
        verbose_name = 'Описание'
    )
    logo = models.ImageField(
        upload_to='logo_image',
        verbose_name='Логотип'
    )
    locations = models.CharField(
        max_length = 255,
        verbose_name = 'Адрес',
        blank =True, null=True
    )
    phone = models.CharField(
        max_length = 255,
        verbose_name = 'Номер телефона',
        blank =True, null=True
    )
    email = models.EmailField(
        verbose_name = 'Почта',
        blank =True, null=True
    )
    instagram = models.URLField(
        verbose_name = 'Инстаграм',
        blank =True, null=True
    )
    twitter = models.URLField(
        verbose_name = 'Вотсап',
        blank =True, null=True
    )
    facebook = models.URLField(
        verbose_name = 'Фейсбук',
        blank =True, null=True
    )
    class Meta:
        verbose_name = 'Основная настройка'
        verbose_name_plural = 'Основные настройки'


class SettingsPhone(models.Model):
    settings = models.ForeignKey(Settings, related_name='phone_title' , on_delete=models.CASCADE)
    phone = models.CharField(
        max_length = 255,
        verbose_name = 'Телефонный номер'
    )
    class Meta:
        unique_together = ('settings', 'phone')

class Slide(models.Model):
    image = ResizedImageField(
        force_format="WEBP",
        quality=100,
        upload_to = 'slide/',
        verbose_name='Фотография',
        blank =True, null=True
    )
    title = RichTextField(
        verbose_name = 'Название'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Слайд на главной странице'
        verbose_name_plural = "Слайды на главной странице"