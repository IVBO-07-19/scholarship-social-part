from django.test import TestCase
import json
import requests
from django.test import Client


def get_access_token():
    r = requests.post('https://suroegin503.eu.auth0.com/oauth/token', data={
        'grant_type': 'password',
        'username': 'testingemail@gmail.com',
        'password': 'TestPassword1_',
        'scope': 'openid profile email',
        'audience': 'https://welcome/',
        'client_id': 'PdkS09Ig0EYVGK9KPYwncjKMGzXnAasI'})
    return r.json()['access_token']


token = get_access_token()
client = Client()

auth_headers = f'Bearer {token}'


def get_user_id():
    r = requests.get('https://suroegin503.eu.auth0.com/userinfo', HTTP_AUTHORIZATION=auth_headers)
    return r.json()['sub']


userId = get_user_id()


def test_not_authorized():
    response = client.get('/api/social/onetime/list/own/')
    assert response.status_code == 401 or response.status_code == 403


def test_get_own_onetime():
    response = client.get('/api/social/onetime/list/own/', headers=auth_headers)
    assert response.status_code == 200
    assert type(response.json()) is list


def test_create_onetime():
    response = client.post('/api/social/onetime/create/', headers=auth_headers, data=json.dumps({
        'title': 'work',
        'date': '2001-01-01',
        'responsible': 'Zuev',
        'is_organizer': False,
        'is_co_organizer': False,
        'is_assistant': True
    }))

    assert response.status_code == 201
    body = response.json()
    assert type(body) is dict

#
# def test_create_article_writer_with_incorrect_place_returns_400():
#     response = client.post('/api/educ_part/article_writers', headers=auth_headers, data=json.dumps({
#         'id': 0,
#         'event_name': 'string',
#         'prize_place': -1,
#         'participation': 'string',
#         'date': '2021-05-13',
#         'scores': 0
#     }))
#
#     assert response.status_code % 100 == 4
