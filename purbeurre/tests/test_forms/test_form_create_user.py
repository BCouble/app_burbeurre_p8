from django.test import TestCase
from purbeurre.forms import CustomUserCreationForm
from purbeurre.libs.constant import LABEL_PASSWORD1


class CreateUserFormTest(TestCase):
    def setUp(self):
        self.form = CustomUserCreationForm()

    def test_form_username_field(self):
        """ Check if form label and help text is valid for usernam """
        self.assertEqual(self.form.fields['username'].label, 'Nom d\'utilisateur ')
        self.assertEqual(self.form.fields['username'].help_text, 'Votre nom d\'utilisateur doit-être unique !')

    def test_form_email_field(self):
        """ Check if form label and help text is valid for e-mail """
        self.assertEqual(self.form.fields['email'].label, 'E-mail ')
        self.assertEqual(self.form.fields['email'].help_text, 'Une adresse mail valide ')

    def test_form_password1_field(self):
        """ Check if form label and help text is valid for password1 """
        self.assertEqual(self.form.fields['password1'].label, 'Votre mot de passe ')
        self.assertEqual(self.form.fields['password1'].help_text, LABEL_PASSWORD1)

    def test_form_password2_field(self):
        """ Check if form label and help text is valid for password2 """
        self.assertEqual(self.form.fields['password2'].label, 'Comfirmez vôtre mot de passe ')
        self.assertEqual(self.form.fields['password2'].help_text, 'Votre mot de passe doit-être identique.')
