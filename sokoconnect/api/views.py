from django.shortcuts import render
from rest_framework import viewsets


from reviews.models import Review
from .serializers import ReviewSerializer




class viewSet(viewsets.ModelViewSet):
   queryset= Review.objects.all()
   serializer_class= ReviewSerializer