from django.test import TestCase, Client
from django.urls import reverse


class IndexPageTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index_returns_200(self):
        response = self.client.get(reverse('purbeurre:index'))
        self.assertEqual(response.status_code, 200)

    def test_signup_returns_200(self):
        response = self.client.get(reverse('purbeurre:signup'))
        self.assertEqual(response.status_code, 200)

    def test_connect_returns_200(self):
        response = self.client.get(reverse('purbeurre:connect'))
        self.assertEqual(response.status_code, 200)

    def test_disconnect_return_302(self):
        response = self.client.get(reverse('purbeurre:user_logout'))
        self.assertEqual(response.status_code, 302)
