from rest_framework import serializers
from users.models import MamaMboga
from users.models import Customer


class MamaMbogaSerializer(serializers.ModelSerializer):
    class Meta:
        model=MamaMboga
        fields="__all__"
        

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields="__all__"

