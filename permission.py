from rest_framework import permissions
from django.contrib.auth.models import Permission


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        adminGroupName = 'LIB-Counter-Reports'
        user_groups = []
        for g in request.user.groups.all():
            user_groups.append(g.name)
        if 'samlUserdata' in request.session:
            samlUserdata = request.session['samlUserdata']
            if "urn:oid:1.3.6.1.4.1.632.11.2.200" in samlUserdata:
                grouper = samlUserdata['urn:oid:1.3.6.1.4.1.632.11.2.200']
                user_groups = list(set(user_groups+grouper))
        user_groups.sort()

        if request.user and adminGroupName in user_groups:
            return True
        return False
