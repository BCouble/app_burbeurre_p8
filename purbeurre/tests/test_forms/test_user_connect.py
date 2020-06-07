from django.test import TestCase, Client
from purbeurre.models import CustomUser
from django.urls import reverse


class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        CustomUser.objects.create_user(username='babatest', password='123AZEr!', email='baba.test@django.me')

    def test_that_user_gets_logged_in(self):
        """ Test user logged """
        response = self.client.post(reverse('purbeurre:connect'),
                                    {
                                        'username': 'babatest',
                                        'password': '123AZEr!'
                                    })
        self.assertEqual(response.url, '/')
