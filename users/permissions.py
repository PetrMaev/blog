from rest_framework import permissions


class IsUserOwner(permissions.BasePermission):
    """Проверяет, является ли пользователь владельцем своего профиля."""

    def has_object_permission(self, request, view, obj):
        if obj.email == request.user.email:
            return True
        return False


class IsSuperUser(permissions.BasePermission):
    """Проверяет, является ли пользователь администратором."""

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False
