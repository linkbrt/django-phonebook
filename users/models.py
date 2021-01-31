from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import phone_regex


class Company(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.CharField(max_length=200,
                                   blank=True, null=True)

    def __str__(self) -> str:
        return self.title


class Profile(AbstractUser):
    """
    Переопределение first_name и last_name
    т.к. фамилия и имя обязательные аргументы
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=50,
                                   blank=True, null=True)
    company = models.ForeignKey(Company,
                                on_delete=models.SET_NULL,
                                related_name='profiles',
                                blank=True, null=True)


class NumberTypeChoise(models.Choices):
    PHONE = 'Phone'
    WHATSAPP = 'WhatsApp'
    TELEGRAM = 'Telegram'


class Number(models.Model):
    type = models.CharField(max_length=30,
                            choices=NumberTypeChoise.choices,
                            default=NumberTypeChoise.PHONE)
    phone_number = models.CharField(validators=[phone_regex],
                                    max_length=15,
                                    blank=True)
    user = models.ForeignKey(Profile,
                             on_delete=models.CASCADE,
                             related_name='numbers')
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.phone_number
