from rest_framework.permissions import BasePermission

class IsAdminOrAuthor(BasePermission):
    
    def has_permission(self, request, view):
        return (request.user.role == "admin" or request.user.role == "author")