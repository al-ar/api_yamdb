from rest_framework.permissions import SAFE_METHODS, BasePermission


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS


class IsSuperUserOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class IsAdminUserOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        role = 'admin'
        if not request.user.is_authenticated:
            return request.method in SAFE_METHODS
        return role == request.user.role


class NotUserRoleOrIsAuthor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user
            or request.user.is_staff
            or request.user.is_superuser
        )


class IsModeratorUser(BasePermission):
    def has_permission(self, request, view):
        role = 'moderator'
        return role == request.user.role


class IsAdminOrSuperuser(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return request.user.is_superuser
        if request.user.is_authenticated:
            role = 'admin'
            return role == request.user.role
