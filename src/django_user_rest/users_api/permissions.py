from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """ Allow user to update own profile only."""

    def has_object_permission(self, request, view, obj):
        """ Checking if user is modifying his own profile."""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class PostOwnStatus(permissions.BasePermission):
    """Allow user to post status on own profile only. """

    def has_object_permission(self, request, view, obj):
        """ This is to check if user is posting/modifying own status."""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
