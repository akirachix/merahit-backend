from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from order.models import Order, OrderItem, Payment, Cart
from inventory.models import Product, Discount
from users.models import Users
from reviews.models import Review
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .daraja import DarajaAPI
from .serializers import (
    STKPushSerializer,
    UsersSerializer,
    ProductSerializer,
    DiscountSerializer,
    OrderSerializer,
    OrderItemSerializer,
    PaymentSerializer,
    CartSerializer,
    ReviewSerializer,
)
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, BasePermission, SAFE_METHODS # Import BasePermission and SAFE_METHODS for DiscountPermission
# Import all custom permission classes
from users.permissions import (
    IsVendor, IsCustomer, IsAdminOrSelf, ProductPermission, ReviewPermission,
    OrderPermission, OrderItemPermission, PaymentPermission, CartPermission
)
# New DiscountPermission class (add this to your users/permissions.py)
class DiscountPermission(BasePermission):
    """
    Access rules for Discounts:
    - Admins have full access.
    - Mamamboga (vendors) can create/update/delete their own discounts.
    - Customers can only read (GET) discounts.
    """
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False
        if user.is_staff:
            return True
        if user.usertype == 'mamamboga':
            return True # Mamamboga can create/manage discounts
        if user.usertype == 'customer':
            return request.method in SAFE_METHODS # Customers can only read
        return False
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_staff:
            return True
        if user.usertype == 'mamamboga':
            # Assuming Discount model has a 'vendor' ForeignKey or similar
            # that links it to the Mamamboga user
            return hasattr(obj, 'vendor') and obj.vendor == user
        if user.usertype == 'customer':
            return request.method in SAFE_METHODS
        return False
class Signup(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        phone = request.data.get('phone_number')
        password = request.data.get('password')
        full_name = request.data.get('full_name')
        usertype = request.data.get('usertype')
        address = request.data.get('address', 'Nairobi, Kenya')
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')
        profile_picture = request.data.get('profile_picture')
        try:
            user = Users(
                phone_number=phone,
                full_name=full_name,
                usertype=usertype,
                address=address,
                latitude=latitude,
                longitude=longitude,
                profile_picture=profile_picture,
            )
            user.set_password(password)
            user.save()
            serialized_user = UsersSerializer(user)
            return Response(serialized_user.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
class Login(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        phone = request.data.get('phone_number')
        password = request.data.get('password')
        user = authenticate(request, phone_number=phone, password=password)
        if user is None:
            return Response({'error': 'Invalid phone number or PIN'}, status=status.HTTP_401_UNAUTHORIZED)
        if not Users.objects.filter(pk=user.pk).exists():
            return Response({'error': 'User does not exist in DB.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            token, created = Token.objects.get_or_create(user=user)
        except Exception as exc:
            return Response({'error': f'Token creation failed: {exc}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({
            'token': token.key,
            'usertype': user.usertype,
            'full_name': user.full_name,
            'phone_number': user.phone_number,
        })
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ReviewPermission]
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [PaymentPermission] # Applied new permission
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [CartPermission] # Applied new permission
class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['usertype']
    permission_classes = [IsAdminOrSelf]
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        for user_data in response.data:
            user_data.pop('till_number', None)
        return response
    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        response.data.pop('till_number', None)
        return response
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [ProductPermission]
class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    permission_classes = [DiscountPermission] # Applied new permission
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [OrderPermission] # Applied new permission
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [OrderItemPermission] # Applied new permission
class STKPushView(APIView):
    def post(self, request):
        serializer = STKPushSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            daraja = DarajaAPI()
            response = daraja.stk_push(
                phone_number=data['phone_number'],
                order_item=data['order_item'],
                amount=data['amount'],
                account_reference=data['account_reference'],
                transaction_desc=data['transaction_desc']
            )
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def daraja_callback(request):
    print("Daraja Callback Data:", request.data)
    return Response({"ResultCode": 0, "ResultDesc": "Accepted"})
    
# @api_view(['POST'])
# def daraja_callback(request):
#     print("Daraja Callback Data:", request.data)
#     return Response({"ResultCode": 0, "ResultDesc": "Accepted"})












