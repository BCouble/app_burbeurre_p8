from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class SearchProductForm(forms.Form):
    """ recherche dans l'openfood et dans les aliment sauvegardé """
    search_text = forms.CharField(max_length=100, required=True)


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


class ConnexionForm(forms.Form):
    """ connect user at platform """
    pass
    """
    username = forms.CharField(
        label="Nom d'utilisateur",
        max_length=30
    )
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput
    )
    """