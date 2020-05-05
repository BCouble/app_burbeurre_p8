from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from .libs.constant import LABEL_PASSWORD1
from .models import CustomUser


class SearchProductForm(forms.Form):
    """ recherche dans l'openfoodfact's bdd et dans les aliments sauvegardé """
    search_text = forms.CharField(max_length=100, required=True)


class CustomUserCreationForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput,
                            help_text=mark_safe('Une adresse mail valide '),
                            label='E-mail ',
                            required=True)
    password1 = forms.CharField(widget=forms.PasswordInput,
                                help_text=mark_safe(LABEL_PASSWORD1),
                                label='Votre mot de passe ')
    password2 = forms.CharField(widget=forms.PasswordInput,
                                help_text=mark_safe('Votre mot de passe doit-être identique.'),
                                label='Comfirmez vôtre mot de passe ')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'background', 'genre']
        labels = {
            'username': _('Nom d\'utilisateur '),
            'genre': _('Monsieur ou Madame '),
            'background': _('Choisissez une couleur pour vôtre profile utilisateur '),
        }
        help_texts = {
            'username': _('Votre nom d\'utilisateur doit-être unique !'),
        }


class CustomUserConnectForm(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput,
                               help_text=mark_safe(''),
                               label='Votre mot de passe ')

    class Meta(AuthenticationForm):
        model = CustomUser
        fields = ['username', 'password']
        labels = {
            'username': _('Nom d\'utilisateur '),
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
