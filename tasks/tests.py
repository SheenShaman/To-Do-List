from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from tasks.models import Task

User = get_user_model()


class TaskTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='test@test.com', password='12345')
        self.refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.refresh.access_token}')

        self.task = Task.objects.create(title='test_task', user=self.user)

    def test_create(self):
        response = self.client.post('/tasks/create/', {'title': 'new task', 'user': self.user.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list(self):
        response = self.client.get(f'/tasks/list/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail(self):
        response = self.client.get(f'/tasks/detail/{self.task.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update(self):
        response = self.client.patch(
            f'/tasks/update/{self.task.id}/',
            {'title': 'update task', 'completed': True}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        response = self.client.delete(f'/tasks/delete/{self.task.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
