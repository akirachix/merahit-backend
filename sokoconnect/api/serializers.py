from rest_framework import serializers
from users.models import Users, Customer, MamaMboga

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            'id',
            'full_name',
            'phone_number',
            'password',
            'latitude',
            'longitude',
            'profile_picture',
            'created_at',
            'updated_at',
            'usertype',
        ]

    def to_representation(self, instance):
        try:
            if instance.usertype == 'customer' and hasattr(instance, 'customer'):
                serializer = CustomerSerializer(instance.customer)
            elif instance.usertype == 'mamamboga' and hasattr(instance, 'mamamboga'):
                serializer = MamaMbogaSerializer(instance.mamamboga)
            else:
                return super().to_representation(instance)
            return serializer.to_representation(instance)
        except (Customer.DoesNotExist, MamaMboga.DoesNotExist):
            return super().to_representation(instance)

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'full_name', 'phone_number', 'latitude', 'longitude', 'profile_picture', 'created_at', 'updated_at', 'usertype', 'is_loyal']

class MamaMbogaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MamaMboga
        fields = ['id', 'full_name', 'phone_number', 'latitude', 'longitude', 'profile_picture', 'created_at', 'updated_at', 'usertype']