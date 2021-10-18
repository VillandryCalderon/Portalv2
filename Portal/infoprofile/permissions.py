from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    # def has_permission(self, request, view):
    #   return False

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        print('has_object_permission')
        raise NotImplementedError
        if request.method in permissions.SAFE_METHODS:
            print('safe method')
            return True
        print(obj.owner == request.user)
        # Instance must have an attribute named `owner`.
        return obj.owner == request.user


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
