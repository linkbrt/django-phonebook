from django.db import models
from django.contrib.auth.models import AbstractUser


class Company(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()

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
                                blank=True, null=True)


class NumberTypeChoise(models.Choices):
    PHONE = 'Phone'
    WHATSAPP = 'WhatsApp'
    TELEGRAM = 'Telegram'


class Number(models.Model):
    type = models.CharField(max_length=30,
                            choices=NumberTypeChoise.choices,
                            default=NumberTypeChoise.PHONE)
    number = models.CharField(max_length=12)
    user = models.ForeignKey(Profile,
                             on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.number
