from rest_framework import permissions
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='LIB-Counter-Reports'):
            return True
        return False
