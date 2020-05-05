import unittest
from purbeurre.forms import SearchProductForm


class SearchProductFormTest(unittest.TestCase):
    """ Test champ of pai's search """
    def test_valid_data(self):
        """ Test if data is valid """
        form = SearchProductForm({
            'search': "nutella",
        })
        self.assertTrue(form.is_valid())

    def test_blank_data(self):
        """ Test if data is not valid """
        form = SearchProductForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'search_text': ['required'],
        })

import unittest
from django.test import TestCase
from purbeurre.forms import CustomUserCreationForm


class CreateUserFormTest(TestCase):
    def test_form_valid(self):
        """ Check if form is valid """
        form = CustomUserCreationForm({
            'username': "babacool",
            'pswd': "3214",
            'valid_pswd': "3214",
            'email': "baba.cool@tata.com",
        })
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        """ test if form is invalid """
        form = CustomUserCreationForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'first_name': ['required'],
            'last_name': ['required'],
            'email': ['required']
        })


if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()
