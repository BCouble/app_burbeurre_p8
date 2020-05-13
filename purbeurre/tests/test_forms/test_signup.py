from django.test import TestCase
from purbeurre.forms import CustomUserCreationForm


class SignupTestForm(TestCase):
    def test_custom_user_valid(self):
        """ valid form creation custom user """
        user = {
            "username": "babatest",
            "password1": "123AZEr!",
            "password2": "123AZEr!",
            "email": "baba.test@django.fr",
            "background": 1,
            'genre': 'O',
        }
        form = CustomUserCreationForm(data=user)
        self.assertTrue(form.is_valid())

    def test_custom_user_not_valid(self):
        """ invalid form creation custom user wrong all fields"""
        userfailall = {
            "username": "@ccz!ù",
            "password1": "123",
            "password2": "123",
            "mail": "baba.test.django",
            'background': 2,
            'genre': 'T',
        }
        form = CustomUserCreationForm(data=userfailall)
        self.assertFalse(form.is_valid())

    def test_custom_user_password_different(self):
        """ test if the passwords are different """
        user = {
            "username": "babatest",
            "password1": "123AZEr!",
            "password2": "123A",
            "email": "baba.test@django.fr",
            "background": 1,
            'genre': 'O',
        }
        form = CustomUserCreationForm(data=user)
        self.assertFalse(form.is_valid())

    def test_custom_user_email_valid(self):
        """ test if the email address is valid """
        user = {
            "username": "babatest",
            "password1": "123AZEr!",
            "password2": "123AZEr!",
            "email": "baba.testdjango",
            "background": 1,
            'genre': 'O',
        }
        form = CustomUserCreationForm(data=user)
        self.assertFalse(form.is_valid())
