from rest_framework.test import APITestCase
from rest_framework import status
from users.models import Users, Customer, MamaMboga

class UsersModelTestCase(APITestCase):
    def test_create_customer(self):
        customer = Customer.objects.create(
            full_name="Test Customer",
            phone_number="1112223333",
            password="pass1234",
            latitude=0.0,
            longitude=0.0,
            profile_picture="http://example.com/customer.jpg",
            is_loyal=True
        )
        self.assertEqual(customer.usertype, 'customer')
        self.assertEqual(customer.full_name, "Test Customer")
        self.assertTrue(customer.is_loyal)
        self.assertIsInstance(customer.created_at, type(customer.updated_at))

    def test_create_mamamboga(self):
        mamamboga = MamaMboga.objects.create(
            full_name="Mama Mboga",
            phone_number="4445556666",
            password="pass5678",
            latitude=1.0,
            longitude=2.0,
            profile_picture="http://example.com/mamamboga.jpg",
            working_days="Mon-Fri",
            working_hours="8am-5pm"
        )
        self.assertEqual(mamamboga.usertype, 'mamamboga')
        self.assertEqual(mamamboga.full_name, "Mama Mboga")
        self.assertEqual(mamamboga.working_days, "Mon-Fri")
        self.assertEqual(mamamboga.working_hours, "8am-5pm")
        self.assertIsInstance(mamamboga.created_at, type(mamamboga.updated_at))

    def test_user_str(self):
        customer = Customer.objects.create(
            full_name="Test Customer",
            phone_number="7778889999",
            password="pass4321",
            latitude=5.0,
            longitude=6.0,
            profile_picture="http://example.com/customer2.jpg"
        )
        mamamboga = MamaMboga.objects.create(
            full_name="Mama Mboga2",
            phone_number="0001112222",
            password="pass8765",
            latitude=9.0,
            longitude=10.0,
            profile_picture="http://example.com/mamamboga2.jpg",
            working_days="Sat-Sun",
            working_hours="9am-4pm"
        )
        self.assertEqual(str(customer), f"Welcome {customer.full_name}")
        self.assertEqual(str(mamamboga), f"Welcome {mamamboga.full_name}")