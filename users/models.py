from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Модель пользователя."""
    username = None
    login = models.CharField(
        max_length=125,
        unique=True,
        verbose_name="Логин",
        help_text="Введите свой логин"
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Email"
    )
    born_date = models.DateField(
        verbose_name="Дата рождения",
        help_text="Укажите свою дату рождения"
    )
    phone_number = models.CharField(
        max_length=25,
        blank=True,
        null=True,
        verbose_name="Номер телефона",
        help_text="Укажите свой номер телефона",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата редактирования"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
