from django import forms


class SearchProductForm(forms.Form):
    """ recherche dans l'openfood et dans les aliment sauvegardé """
    pass
    """ 
    search_text = forms.CharField(
        label="alimentà substituer ",
        max_length=100
    )
    """


class CreateUserForm(forms.Form):
    """ create user for purbeurre platform """
    pass
    """
    first_name(user django)
    last_name(user django)
    email(user django)
    img_choix (background vue profil)
    genre (CheckboxInput : homme ou femme)
    """


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