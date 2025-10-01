from rest_framework import permissions


class IsAuthor(permissions.BasePermission):
    """Проверяет, является ли пользователь автором комментария."""

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user.email:
            return True
        return False


class IsOwner(permissions.BasePermission):
    """Проверяет, является ли пользователь автором поста."""

    def has_object_permission(self, request, view, obj):
        if obj.owner.email == request.user.email:
            return True
        return False
