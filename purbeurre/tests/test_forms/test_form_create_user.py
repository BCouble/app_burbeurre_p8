import unittest
from django.contrib.auth import get_user_model
from purbeurre.forms import CreateUserForm
from purbeurre.models import Profil


class CreateUserFormTest(unittest.TestCase):
    def setUp(self):
        self.profil = Profil.objects.create(email="baba.cool@tata.com")


    def test_init(self):
        CreateUserForm(entry=self.profil)

    def test_init_with_search_text(self):
        with self.assertRaises(KeyError):
            CreateUserForm()

    def test_valid_data(self):
        form = CreateUserForm({
            'first_name': "baba",
            'last_name': "cool",
            'pswd': "3214",
            'valid_pswd': "3214",
            'email': "baba.cool@tata.com",
        })
        self.assertTrue(form.is_valid())

    def test_blank_data(self):
        form = CreateUserForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'first_name': ['required'],
            'last_name': ['required'],
            'email': ['required']
        })


if __name__ == '__main__':
    unittest.main()
