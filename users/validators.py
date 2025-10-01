import re

from rest_framework import serializers


class EmailValidator:
    __fields__ = ['email']

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        mail = dict(value).get(self.field)
        if (bool(re.search(r'\w*mail.ru', mail)) is False and
                bool(re.search(r'\w*yandex.ru', mail)) is False):
            raise serializers.ValidationError(
                'Используйте только разрешенные домены: mail.ru, yandex.ru'
            )


class PasswordValidator:
    __fields__ = ['password']

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        password = dict(value).get(self.field)
        if password:
            if len(password) < 8:
                raise serializers.ValidationError(
                    'Пароль должен иметь не менее 8 символов'
                )
            else:
                if not bool(re.search(r'\d', password)):
                    raise serializers.ValidationError(
                        'Пароль должен содержать цифры'
                    )
