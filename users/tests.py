from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient

User = get_user_model()


class UserTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='test@test.com', password='12345')

    def test_login(self):
        response = self.client.post('/users/token/', {'email': 'test@test.com', 'password': '12345'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_token_refresh(self):
        get_token = self.client.post('/users/token/', {'email': 'test@test.com', 'password': '12345'})
        response = self.client.post('/users/token/refresh/', {'refresh': get_token.data['refresh']})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
