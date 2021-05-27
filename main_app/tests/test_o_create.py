import requests

from .setup import TestSetUp


class Test(TestSetUp):
    route = f'/api/social/onetime/create/'

    def test_anauthorized(self):
        response = self.client.post(self.route)

        self.assertEqual(response.status_code, 401)

    def test_invalid_token(self):
        self.client.credentials(HTTP_AUTHORIZATION='lol_kek')
        response = self.client.post(self.route)

        self.assertEqual(response.status_code, 401)

    def test_with_closed_application(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.STUDENT)
        self.create_aplication()
        requests.post('https://secure-gorge-99048.herokuapp.com/api/application/close/',
                      headers={'Authorization': TestSetUp.STUDENT})
        data = {
            'title': 'string',
            'work': 'string',
            'responsible': 'string',
            'is_organizer': True,
            'is_co_organizer': False,
            'is_assistant': False,
            'date': '2021-01-01'
        }
        response = self.client.post(self.route, data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), 'ur application is closed')

    def test_without_data(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.STUDENT)
        self.create_aplication()
        response = self.client.post(self.route)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), 'send full info')

    def test_without_application(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.ADMIN)
        data = {
            'title': 'cool work',
            'work': 'yes',
            'responsible': 'Zuev',
            'is_organizer': '',
            'is_co_organizer': '',
            'is_assistant': True,
            'date': '2021-01-01'
        }
        response = self.client.post(self.route, data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), 'create application in central service')

    def test_incorrect_data(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.STUDENT)
        self.create_aplication()
        data = {
            'title': 1,
            'work': 1,
            'responsible': 1,
            'is_organizer': 'lol',
            'is_co_organizer': 'lol',
            'is_assistant': 'lol',
            'date': 5
        }
        response = self.client.post(self.route, data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), 'change date to correct')

    def test_incorrect_participation_level(self):
        self.create_aplication()
        self.client.credentials(HTTP_AUTHORIZATION=self.STUDENT)
        data = {
            'title': 'string',
            'work': 'string',
            'responsible': 'string',
            'is_organizer': False,
            'is_co_organizer': False,
            'is_assistant': False,
            'date': '2021-01-01'
        }
        response = self.client.post(self.route, data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), 'fix ur participation level')

    def test_valid(self):
        self.create_aplication()
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
        response = self.client.post(self.route, data)
        self.assertEqual(response.status_code, 201)
