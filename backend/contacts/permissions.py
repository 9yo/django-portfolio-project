from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, object):
        if request.user:
            if request.user.is_superuser:
                return True
            else:
                return object.owner == request.user

        else:
            return False
