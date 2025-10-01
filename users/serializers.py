from rest_framework import serializers

from users.models import CustomUser
from users.validators import EmailValidator, PasswordValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "login", "born_date", "email", "phone_number"]
        validators = [EmailValidator(field="email")]


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["login", "email", "born_date", "phone_number", "password"]
        extra_kwargs = {"password": {"write_only": True}}
        validators = [EmailValidator(field="email"), PasswordValidator(field="password")]
