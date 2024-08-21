from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    '''
    Only admin users can access this view.
    '''
    def has_permission(self, request, view):
        return request.user.is_superuser
