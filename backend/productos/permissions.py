from rest_framework import permissions
from .groups import is_user_in_group

class isAle(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ('GET','POST','PUT','HEAD','DELETE','PATCH'):
            return False
        return request.user and is_user_in_group(request.user, 'ale')  #solo puede usar el metodo OPTIONS XD