from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from users.models import Users, Customer, MamaMboga

class UsersModelTest(TestCase):
    def test_create_user(self):
        user = Users.objects.create(
            full_name="Test User",
            phone_number="0712345678",
            password="pass1234",
            latitude=1.2345,
            longitude=2.3456,
            profile_picture="http://example.com/pic.jpg"
        )
        self.assertEqual(user.full_name, "Test User")
        self.assertEqual(user.phone_number, "0712345678")

class CustomerModelTest(TestCase):
    def test_create_customer_and_str(self):
        customer = Customer.objects.create(
            full_name="Jane Customer",
            phone_number="0798765432",
            password="pass5678",
            latitude=3.21,
            longitude=1.23,
            profile_picture="http://example.com/pic2.jpg",
            is_loyal=True
        )
        self.assertTrue(customer.is_loyal)
        self.assertEqual(str(customer), "Welcome Jane Customer")

class MamaMbogaModelTest(TestCase):
    def test_create_mamamboga_and_str(self):
        mama = MamaMboga.objects.create(
            full_name="Mama Mboga",
            phone_number="0700111222",
            password="mboga123",
            latitude=-1.0,
            longitude=36.8,
            profile_picture="http://example.com/mama.jpg",
            working_days="Monday-Friday",
            working_hours="8am-5pm"
        )
        self.assertEqual(mama.working_days, "Monday-Friday")
        self.assertEqual(mama.working_hours, "8am-5pm")
        self.assertEqual(str(mama), "Welcome Mama Mboga")