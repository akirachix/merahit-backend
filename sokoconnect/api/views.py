from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from order.models import Order, OrderItem, Payment, Cart
from inventory.models import Product, Discount
from users.models import Users, Customer, MamaMboga
from reviews.models import Review
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .daraja import DarajaAPI
from .serializers import STKPushSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .geocoding import geocode_address, reverse_geocode

from .serializers import (
    UsersSerializer,
    MamaMbogaSerializer,
    CustomerSerializer,
    ProductSerializer,
    DiscountSerializer,
    OrderSerializer,
    OrderItemSerializer,
    PaymentSerializer,
    CartSerializer,
    ReviewSerializer,
)

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['usertype']


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


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



def geocode_view(request):
    address = request.GET.get('address')
    if not address:
        return JsonResponse({'error': 'Address is required'}, status=400)
    
    result = geocode_address(address)
    if result:
        return JsonResponse(result)
    return JsonResponse({'error': 'Geocoding failed'}, status=500)

def reverse_geocode_view(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    if not (lat and lon):
        return JsonResponse({'error': 'Latitude and longitude are required'}, status=400)
    
    result = reverse_geocode(lat, lon)
    if result:
        return JsonResponse({'address': result})
    return JsonResponse({'error': 'Reverse geocoding failed'}, status=500)
