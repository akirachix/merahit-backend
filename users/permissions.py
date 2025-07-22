from rest_framework.permissions import BasePermission, SAFE_METHODS
class IsVendor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.usertype == 'mamamboga'
class IsCustomer(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.usertype == 'customer'
class IsAdminOrSelf(BasePermission):
   
    def has_permission(self, request, view):
        if getattr(view, "action", None) == "list":
            return request.user.is_authenticated and request.user.is_staff
        return request.user.is_authenticated
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj == request.user
class ProductPermission(BasePermission):
    """
    Allow full access only to mamamboga users and staff,
    and read-only access to customers.
    """
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False
        if user.is_staff or user.usertype == 'mamamboga':
            return True
        if user.usertype == 'customer' and request.method in SAFE_METHODS:
            return True 
        return False 

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_staff or user.usertype == 'mamamboga':
            return True
        if user.usertype == 'customer' and request.method in SAFE_METHODS:
            return True
        return False


class ReviewPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False
        if user.is_staff:
            return True
        if user.usertype == 'mamamboga':
            return request.method in SAFE_METHODS
        if user.usertype == 'customer':
            return True 
        return False

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_staff:
            return True
        if user.usertype == 'mamamboga':
            return request.method in SAFE_METHODS and obj.vendor == user

        if user.usertype == 'customer':
            return obj.customer == user
            
        return False

class OrderPermission(BasePermission):
   
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_staff:
            return True
        if user.usertype == 'mamamboga':
            return obj.vendor_id == user.id
        if user.usertype == 'customer':
            return obj.customer_id == user.id
        return False

class OrderItemPermission(BasePermission):
  
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_staff:
            return True
        if user.usertype == 'mamamboga':
            return obj.order.vendor_id == user.id
        if user.usertype == 'customer':
            return obj.order.customer_id == user.id
        return False

class PaymentPermission(BasePermission):
 
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        user = request.user
        order = obj.order
        if user.is_staff:
            return True
        if user.usertype == 'mamamboga':
            return order.vendor_id == user.id
        if user.usertype == 'customer':
            return order.customer_id == user.id
        return False

class CartPermission(BasePermission):
 
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_staff:
            return True
        if user.usertype == 'customer':
            return obj.customer_id == user.id
        return False

