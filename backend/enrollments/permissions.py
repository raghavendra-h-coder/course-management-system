from rest_framework.permissions import BasePermission
from accounts.models import Role

class IsAuthenticatedStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in (Role.STUDENT, Role.ADMIN)