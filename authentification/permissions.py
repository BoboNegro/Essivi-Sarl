from rest_framework import permissions

class IsStaffPermissions(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        return super().has_permission(request, view)