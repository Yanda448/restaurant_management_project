from rest_framework.permissions import BasePermission

class IsManagerOrAdmin(BasePermission):
    """Only Manager or Admin can add/edit menu items."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['Manager', 'Admin']

class IsWaiter(BasePermission):
    """Only Waiter can create orders."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'Waiter'

class IsCashier(BasePermission):
    """Only Cashier can process payments."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'Cashier'