<<<<<<< HEAD
=======
from rest_framework.test import APITestCase
from django.urls import reverse
from users.models import Customer, MamaMboga
from reviews.models import Review


class ReviewAPITest(APITestCase):
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


   def test_vendor_review_api_crud(self):
       url = reverse('feedback-list')
       data = {
           "vendor": self.vendor.id,
           "customer": self.customer.id,
           "rating": 5,
           "comment": "Awesome experience!"
       }
       response = self.client.post(url, data, format='json')
       self.assertEqual(response.status_code, 201)
       review_id = response.data['id']


       response = self.client.get(url)
       self.assertEqual(response.status_code, 200)
       self.assertEqual(len(response.data), 1)


       detail_url = reverse('feedback-detail', args=[review_id])
       response = self.client.get(detail_url)
       self.assertEqual(response.status_code, 200)
       self.assertEqual(response.data['comment'], "Awesome experience!")


       updated_data = {
           "vendor": self.vendor.id,
           "customer": self.customer.id,
           "rating": 4,
           "comment": "Updated review"
       }
       response = self.client.put(detail_url, updated_data, format='json')
       self.assertEqual(response.status_code, 200)
       self.assertEqual(response.data['rating'], 4)
       self.assertEqual(response.data['comment'], "Updated review")


       response = self.client.delete(detail_url)
       self.assertEqual(response.status_code, 204)
       response = self.client.get(detail_url)
       self.assertEqual(response.status_code, 404)
>>>>>>> f48c93d (Created Reviews api endpoints and tested it)
