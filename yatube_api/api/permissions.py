from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Разрешение: автор может редактировать/удалять свой контент,
    остальным только чтение.
    """
    def has_permission(self, request, view):
        # Проверяем, что пользователь аутентифицирован
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Чтение разрешено всем аутентифицированным
        if request.method in permissions.SAFE_METHODS:
            return True
        # Изменение/удаление только автору
        return obj.author == request.user
