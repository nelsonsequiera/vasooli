from rest_framework import permissions
from gale_user.models import User


class IsManager(permissions.BasePermission):
    message = 'You do not have access here. fuck off.'

    def has_permission(self, request, view):
        user = User.objects.get(username=request.user.username)
        print user.is_manager
        if user.is_manager is True:
            return True
        else:
            return False
