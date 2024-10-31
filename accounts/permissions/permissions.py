from rest_framework import permissions


class IsManagement(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Management').exists()

class IsEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Employee').exists()