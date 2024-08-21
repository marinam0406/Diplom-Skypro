from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import User


class UserAPITestCase(APITestCase):
    '''
    Test class for User API endpoints.
    '''
    def setUp(self):
        '''
        Create a test user for the API test.
        '''
        self.client = APIClient()
        self.user_data = {
            'email': 'test@example.com',
            'password': 'testpassword'
        }
        self.url = reverse("users:users-list")

    def test_create_user(self):
        '''
        Test creating a new user using the API.
        '''
        response = self.client.post(self.url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(email=self.user_data['email'])
        self.assertTrue(user.check_password(self.user_data['password']))
        self.assertEqual(user.email, self.user_data['email'])

    def test_get_list_of_users(self):
        '''
        Test retrieving a list of users using the API.
        '''
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_details(self):
        '''
        Test retrieving user details using the API.
        '''
        user = User.objects.create(**self.user_data)
        response = self.client.get(f'{self.url}{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
