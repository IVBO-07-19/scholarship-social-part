import requests

from .setup import TestSetUp


class Test(TestSetUp):
    def route(self, pk):
        return f'/api/social/onetime/{pk}/'

    def create(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.STUDENT)
        data = {
            'title': 'cool work',
            'work': 'yes',
            'responsible': 'Zuev',
            'is_organizer': '',
            'is_co_organizer': '',
            'is_assistant': True,
            'date': '2021-01-01'
        }
        self.client.post('/api/social/onetime/create/', data)

    def test_anauthorized(self):
        response = self.client.get(self.route(1))

        self.assertEqual(response.status_code, 401)

    def test_invalid_token(self):
        self.client.credentials(HTTP_AUTHORIZATION='lol_kek')
        response = self.client.get(self.route(1))

        self.assertEqual(response.status_code, 401)

    def test_not_users_app(self):
        self.create_aplication()
        self.create()
        self.client.credentials(HTTP_AUTHORIZATION=self.ADMIN)
        response = self.client.get(self.route(1))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), 'does not exist')

    def test_valid(self):
        self.create_aplication()
        self.create()
        self.client.credentials(HTTP_AUTHORIZATION=self.STUDENT)
        response = self.client.get(self.route(1))
        self.assertEqual(response.status_code, 200)
