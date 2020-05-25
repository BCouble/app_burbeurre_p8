from django.db import models
from django.contrib.auth.models import AbstractUser


class Message(models.Model):
    message_txt = models.CharField(max_length=200)

    def __str__(self):
        return self.message_txt


class CustomUser(AbstractUser):
    """ Custom User for background profile and genre add """
    FEMALE = 'F'
    MALE = 'M'
    NULL = 'O'
    GENRE_CHOICES = [(FEMALE, 'femme'), (MALE, 'homme'), (NULL, 'non définit'), ]
    genre = models.CharField(max_length=2, choices=GENRE_CHOICES, default=NULL, )
    BG1 = '1'
    BG2 = '2'
    BG3 = '3'
    BACKGROUND_CHOICES = [(BG1, 'Rose'), (BG2, 'Vert'), (BG3, 'Orange'), ]
    background = models.CharField(max_length=1, choices=BACKGROUND_CHOICES, default=BG1, )


class Category(models.Model):
    """ Model catégory niv 0 off """
    name = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey('Category', on_delete=models.CASCADE, related_name="children", null=True)

    def __str__(self):
        return self.name


class FoodPurBeurre(models.Model):
    """ Model Food of OpenFoodFact """
    product_name_fr = models.CharField(max_length=255, unique=True)
    generic_name_fr = models.CharField(max_length=400)
    nutriscore = models.CharField(max_length=1)
    nut_cent_gr = models.IntegerField()
    store = models.CharField(max_length=200, null=True)
    category_s1 = models.ForeignKey(Category, on_delete=models.CASCADE)
    link_off = models.URLField(max_length=300)
    link_img = models.URLField(max_length=300)

    def __str__(self):
        return self.product_name_fr


class Favoris(models.Model):
    """ Save Favoris for user """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    food = models.ForeignKey(FoodPurBeurre, on_delete=models.CASCADE)
