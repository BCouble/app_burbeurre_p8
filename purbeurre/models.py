from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    message_txt = models.CharField(max_length=200)

    def __str__(self):
        return self.message_txt


class Profil(models.Model):
    """ Data for user add with User Django genre and background select """
    pass
    #user = models.OneToOneField(User)
    """
    genre = models.fields
    background = models.image
    """


class ProductOpenFoodFact(models.Model):
    """ Data save for favoris's user """
    pass
    """
    name
    nutriscore
    repere nutritionnel pour 100g
    lien page sur l'aliment openfoodfact
    image ou lien image
    id ou référence aliment recherché
    user
    """
