from django.test import TestCase
from users.models import Customer, MamaMboga
from reviews.models import VendorReview

class VendorReviewModelTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            full_name="Test Customer",
            phone_number="0712345678",
            password="pass1234",  
            latitude=1.2345,
            longitude=2.3456,
            profile_picture="http://example.com/profile.jpg"
        )
        self.vendor = MamaMboga.objects.create(
            full_name="Test Vendor",
            phone_number="0798765432",
            password="venpass1",
            latitude=3.4567,
            longitude=4.5678,
            profile_picture="http://example.com/vendor.jpg",
            working_days="Monday-Friday",
            working_hours="8am-6pm"
        )

    def test_vendor_review_creation(self):
        review = VendorReview.objects.create(
            vendor=self.vendor,
            customer=self.customer,
            rating=5,
            comment="Great vendor, fresh vegetables!"
        )
        self.assertEqual(review.vendor, self.vendor)
        self.assertEqual(review.customer, self.customer)
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.comment, "Great vendor, fresh vegetables!")
        self.assertIsNotNone(review.created_at)
        self.assertEqual(str(review), f"Review for {self.vendor.full_name}")