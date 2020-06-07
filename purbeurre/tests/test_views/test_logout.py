from django.test import TestCase, Client
from purbeurre.models import CustomUser
from django.urls import reverse


class LogoutViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_that_user_gets_logout(self):
        """ Test if logout """
        CustomUser.objects.create_user(username='babatest', password='123AZEr!', email='baba.test@django.me')
        self.client.post(reverse('purbeurre:connect'),
                         {
                             'username': 'babatest',
                             'password': '123AZEr!'
                         })
        response = self.client.get(reverse('purbeurre:user_logout'))
        self.assertEqual(response.url, '/')
