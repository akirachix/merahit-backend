from rest_framework.test import APITestCase
from django.urls import reverse
from users.models import MamaMboga, Customer

class MamaMbogaAPITestCase(APITestCase):
    def setUp(self):
        self.url = reverse('mamamboga-list')
        self.data = {
            "full_name": "Mama Mboga",
            "phone_number": "0700111222",
            "password": "pass1234",
            "latitude": -1.0,
            "longitude": 36.8,
            "profile_picture": "http://example.com/mama.jpg",
            "working_days": "Monday-Friday",
            "working_hours": "8am-5pm"
        }

    def test_create_mamamboga(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(MamaMboga.objects.count(), 1)

    def test_list_mamamboga(self):
        MamaMboga.objects.create(**self.data)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

class CustomerAPITestCase(APITestCase):
    def setUp(self):
        self.url = reverse('customer-list')
        self.data = {
            "full_name": "John Doe",
            "phone_number": "0798765432",
            "password": "pass5678",
            "latitude": 3.21,
            "longitude": 1.23,
            "profile_picture": "http://example.com/pic2.jpg",
            "is_loyal": True
        }

    def test_create_customer(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Customer.objects.count(), 1)

    def test_list_customers(self):
        Customer.objects.create(**self.data)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)