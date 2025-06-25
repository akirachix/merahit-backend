from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import MamaMboga, Customer
from inventory.models import Product, Discount
from django.utils import timezone
from datetime import timedelta

class APIMainTests(APITestCase):
    def setUp(self):
        self.mama = MamaMboga.objects.create(
            full_name="Mama Mboga 1",
            phone_number="1234567890",
            password="pass1234",
            latitude=0.123,
            longitude=36.987,
            profile_picture="http://example.com/profile1.jpg",
            working_days="Mon-Fri",
            working_hours="8am-5pm"
        )
        self.customer = Customer.objects.create(
            full_name="Customer 1",
            phone_number="0987654321",
            password="custpas2",
            latitude=0.321,
            longitude=36.123,
            profile_picture="http://example.com/customer1.jpg",
            is_loyal=True
        )
        self.product = Product.objects.create(
            vendor=self.mama,
            product_name="Spinach",
            category="Vegetable",
            price=50.00,
            stock_quantity=100,
            stock_unit="bunch",
            product_image="http://example.com/spinach.jpg",
            description="Fresh spinach"
        )
        self.discount = Discount.objects.create(
            vendor=self.mama,
            product=self.product,
            old_price=70.00,
            new_price=50.00,
            start_date=timezone.now(),
            end_date=timezone.now() + timedelta(days=3)
        )

    def test_list_product(self):
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_product(self):
        url = reverse('product-list')
        data = {
            'vendor': self.mama.id,
            'product_name': 'Kale',
            'category': 'Vegetable',
            'price': 30.00,
            'stock_quantity': 50,
            'stock_unit': 'bunch',
            'product_image': 'http://example.com/kale.jpg',
            'description': 'Fresh kale'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_discount(self):
        url = reverse('discount-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_discount(self):
        url = reverse('discount-list')
        data = {
            'vendor': self.mama.id,
            'product': self.product.id,
            'old_price': 80.00,
            'new_price': 60.00,
            'start_date': timezone.now().isoformat(),
            'end_date': (timezone.now() + timedelta(days=2)).isoformat()
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)