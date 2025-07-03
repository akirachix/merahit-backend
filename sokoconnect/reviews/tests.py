def test_vendor_review_api_crud(self):
    url = '/Review/'
    data = {
        "vendor_id": self.vendor.id,
        "customer_id": self.customer.id,
        "rating": 5,
        "comment": "Awesome experience"
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, 201)
    review_id = response.data['id']

    detail_url = f'/Review/{review_id}/'
    response = self.client.get(detail_url)
    self.assertEqual(response.status_code, 200)

    updated_data = {
        "vendor_id": self.vendor.id,
        "customer_id": self.customer.id,
        "rating": 4,
        "comment": "Updated review"
    }
    response = self.client.put(detail_url, updated_data, format='json')
    self.assertEqual(response.status_code, 200)

    response = self.client.delete(detail_url)
    self.assertEqual(response.status_code, 204)