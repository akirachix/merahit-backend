from rest_framework.test import APITestCase
from rest_framework import status
from users.models import Users
from django.urls import reverse


class AgentManagementTestCase(APITestCase):
    """
    Test case demonstrating why AgentViewSet might not be needed.
    Shows how to use existing UsersViewSet for agent management.
    """

    def setUp(self):
        # Create test users with agent usertype
        self.agent1 = Users.objects.create(
            full_name="Agent Smith",
            phone_number="1234567890",
            usertype="agent"
        )
        self.agent2 = Users.objects.create(
            full_name="Agent Johnson",
            phone_number="0987654321",
            usertype="agent"
        )
        # Create a non-agent user for comparison
        self.customer = Users.objects.create(
            full_name="Regular Customer",
            phone_number="5555555555",
            usertype="customer"
        )

    def test_list_agents_using_users_viewset_filtering(self):
        """
        Test listing agents using the existing UsersViewSet with filtering.
        This shows that AgentViewSet is not necessary for basic agent listing.
        """
        url = reverse('users-list')
        response = self.client.get(url, {'usertype': 'agent'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        for user_data in response.data:
            self.assertEqual(user_data['usertype'], 'agent')

    def test_list_agents_using_users_custom_action(self):
        """
        Test the custom list_agents action in UsersViewSet.
        This demonstrates adding agent-specific functionality to existing ViewSet.
        """
        url = reverse('users-list-agents')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_list_all_users_includes_agents(self):
        """
        Test that listing all users includes agents along with other user types.
        """
        url = reverse('users-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)  # 2 agents + 1 customer
        
        user_types = [user['usertype'] for user in response.data]
        self.assertIn('agent', user_types)
        self.assertIn('customer', user_types)

    def test_create_agent_via_users_signup(self):
        """
        Test creating an agent using the existing users signup endpoint.
        This shows that separate agent creation endpoint is not needed.
        """
        url = reverse('signup')
        data = {
            'full_name': 'New Agent via Users',
            'phone_number': '1111111111',
            'password': 'testpass123',
            'usertype': 'agent',
            'address': 'Test Address'
        }
        
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Verify the user was created with correct type
        user = Users.objects.get(phone_number='1111111111')
        self.assertEqual(user.usertype, 'agent')
        self.assertEqual(user.full_name, 'New Agent via Users')

    def test_filter_excludes_non_agents(self):
        """
        Test that filtering by agent usertype excludes other user types.
        """
        url = reverse('users-list')
        response = self.client.get(url, {'usertype': 'agent'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        
        # Ensure no customers are included
        for user_data in response.data:
            self.assertNotEqual(user_data['usertype'], 'customer')
            self.assertEqual(user_data['usertype'], 'agent')