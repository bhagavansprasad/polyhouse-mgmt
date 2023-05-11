import json
from django.test import TestCase, Client
from django.urls import reverse
from django.http import HttpResponseBadRequest

class appisTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_create_task(self):
        url = reverse('create_task')
        data = {'name': 'John', 'age': 30}
        response = self.client.post(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), 'Hello, John! You are 30 years old.\n')

    def test_create_task_missing_name(self):
        url = reverse('create_task')
        data = {'age': 30}
        response = self.client.post(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), 'Hello, Unknown! You are 30 years old.\n')

    def test_create_task_invalid_json(self):
        url = reverse('create_task')
        data = 'not a valid json string'
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, HttpResponseBadRequest.status_code)
