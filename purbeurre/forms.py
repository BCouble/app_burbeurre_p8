from django import forms
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from .libs.constant import LABEL_PASSWORD1
from .models import CustomUser


class SearchProductForm(forms.Form):
    """ recherche dans l'openfoodfact's bdd et dans les aliments sauvegardé """
    search_text = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rechercher un produit'}),
                                  max_length=100, required=True)

    def get_absolute_url(self):
        return reverse('search_foods', kwargs={'pk': self.pk})


class CustomUserCreationForm(UserCreationForm):
    error_css_class = 'alert alert-primary'
    required_css_class = 'required'

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'mt-4 form-control', 'placeholder': 'Nom d\'utilisateur'}),
                                label='Nom d\'utilisateur')
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'mt-4 form-control', 'placeholder': 'Adresse mail'}),
                            label='E-mail ', required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'mt-4 form-control', 'placeholder': 'Mot de passe'}),
                                label='Votre mot de passe ')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'mt-4 form-control', 'placeholder': 'Confirmer mot de passe'}),
                                label='Comfirmez vôtre mot de passe ')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']


class CustomUserConnectForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'mt-4 form-control', 'placeholder': 'login'}),
                               help_text=mark_safe(''), label='Nom d\'utilisateur ')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'mt-4 form-control', 'placeholder': 'password'}),
                               help_text=mark_safe(''), label='Votre mot de passe ')

    class Meta(AuthenticationForm):
        model = CustomUser
        fields = ['username', 'password']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
