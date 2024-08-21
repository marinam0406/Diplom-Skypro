from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from users.models import User
from .models import EduModel


class EduModelAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email='admin@test.com', password='123', is_staff=True,
                                        is_superuser=True)
        self.client.force_authenticate(user=self.user)
        self.model_data = {
            'number': 1,
            'name': 'Test Model',
            'description': 'This is a test model',
        }
        self.create_url = '/models/create/'
        self.update_url = '/models/update/'
        self.delete_url = '/models/delete/'

    def test_create_model(self):
        response = self.client.post(self.create_url, self.model_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(EduModel.objects.count(), 1)
        self.assertEqual(EduModel.objects.get().name, self.model_data['name'])

    def test_get_list_of_models(self):
        EduModel.objects.create(**self.model_data)
        response = self.client.get('/models/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_update_model(self):
        model = EduModel.objects.create(**self.model_data)
        updated_data = {
            'number': 2,
            'name': 'Updated Model',
            'description': 'This is an updated model',
        }
        response = self.client.put(f'{self.update_url}{model.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        model.refresh_from_db()
        self.assertEqual(model.name, updated_data['name'])

    def test_delete_model(self):
        model = EduModel.objects.create(**self.model_data)
        response = self.client.delete(f'{self.delete_url}{model.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(EduModel.objects.filter(id=model.id).exists())
