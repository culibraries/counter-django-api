from rest_framework import permissions
from django.contrib.auth.models import Permission


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        print(request.user)
        print(request.user.groups)
        if request.user and request.user.groups.filter(name='LIB-Counter-Reports').exists():
            return True
        return False
