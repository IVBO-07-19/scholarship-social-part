from .setup import TestSetUp


class Test(TestSetUp):
    def route(self, pk):
        return f'/api/social/article/rate/{pk}/'

    def create(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.STUDENT)
        data = {
            'title': 'string',
            'media_title': 'string',
            'edition_level_choicer': 'university',
            'co_author_quantity': 1,
            'date': '2021-01-01'
        }
        self.client.post('/api/social/article/create/', data)

    def test_anauthorized(self):
        self.create()
        response = self.client.put(self.route(1))

        self.assertEqual(response.status_code, 403)

    def test_invalid_token(self):
        self.create()
        self.client.credentials(HTTP_AUTHORIZATION='lol_kek')
        response = self.client.put(self.route(1))

        self.assertEqual(response.status_code, 401)

    def test_wrong_id(self):
        self.create()
        self.create_aplication()
        self.client.credentials(HTTP_AUTHORIZATION=self.ADMIN)
        data = {
            'scores': 2,
        }
        response = self.client.put(self.route(100), data)
        self.assertEqual(response.status_code, 400)

    def test_valid(self):
        self.create()
        self.create_aplication()
        self.client.credentials(HTTP_AUTHORIZATION=self.ADMIN)
        data = {
            'scores': 2,
        }
        response = self.client.put(self.route(1), data)
        self.assertEqual(response.status_code, 200)
