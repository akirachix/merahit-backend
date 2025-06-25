from django.shortcuts import render

from rest_framework import viewsets
from users.models import MamaMboga, Customer
from .serializers import MamaMbogaSerializer, CustomerSerializer



class MamaMbogaViewSet(viewsets.ModelViewSet):
    queryset=MamaMboga.objects.all()
    serializer_class=MamaMbogaSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer

