from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """ Allow user to update his profile only."""

    def has_object_permission(self, request, view, obj):
        """ Checking if user is modifying his own profile."""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
