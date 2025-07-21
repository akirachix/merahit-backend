from rest_framework.permissions import BasePermission, SAFE_METHODS
class IsVendor(BasePermission):
    """Allows access only to vendor users."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'vendor'
class IsCustomer(BasePermission):
    """Allows access only to customer users."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'customer'
class IsAdminOrSelf(BasePermission):
    """
    Allows access only to admins or the user themselves (object-level permission).
    Only admins can list all users.
    """
    def has_permission(self, request, view):
        if getattr(view, "action", None) == "list":
            return request.user.is_authenticated and request.user.is_staff
        return request.user.is_authenticated
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj == request.user
class ProductPermission(BasePermission):
    """
    Vendors and admins have full access.
    Customers can only read (GET).
    """
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False
        if user.is_staff or user.role == 'vendor':
            return True
        if user.role == 'customer' and request.method in SAFE_METHODS:
            return True
        return False
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_staff or user.role == 'vendor':
            return True
        if user.role == 'customer' and request.method in SAFE_METHODS:
            return True
        return False
class ReviewPermission(BasePermission):
    """
    Admins have full access.
    Vendors can read reviews of their own products only.
    Customers can CRUD their own reviews.
    """
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False
        if user.is_staff:
            return True
        if user.role == 'vendor':
            return request.method in SAFE_METHODS
        if user.role == 'customer':
            return True
        return False
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_staff:
            return True
        if user.role == 'vendor':
            return hasattr(obj, "product") and getattr(obj.product, "vendor_id", None) == user.id and request.method in SAFE_METHODS
        if user.role == 'customer':
            return hasattr(obj, "customer_id") and obj.customer_id == user.id
        return False