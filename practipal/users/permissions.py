from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == 'Admin')


class IsTherapist(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == 'Therapist')


class IsClient(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == 'Client')
