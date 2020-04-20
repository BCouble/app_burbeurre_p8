from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Message(models.Model):
    message_txt = models.CharField(max_length=200)

    def __str__(self):
        return self.message_txt

class CustomUserManager(UserManager):
    pass

class CustomUser(AbstractUser):
    pass

"""
class Profile(models.Model):
     Data for user add with User Django genre and background select 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    FEMALE = 'F'
    MALE = 'M'
    NULL = 'O'
    GENRE_CHOICES = [
        (FEMALE, 'femme'),
        (MALE, 'homme'),
        (NULL, 'non définit'),
    ]
    genre = models.CharField(
        max_length=2,
        choices=GENRE_CHOICES,
        default=NULL,
    )
    BG1 = '1'
    BG2 = '2'
    BG3 = '3'
    BACKGROUND_CHOICES = [
        (BG1, 'Rose'),
        (BG2, 'Vert'),
        (BG3, 'Orange'),
    ]
    background = models.CharField(
        max_length=1,
        choices=BACKGROUND_CHOICES,
        default=BG1,
    )"""

"""
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()
    """
"""
# P5 !!!
#class ProductOpenFoodFact(models.Model):
     Data save for favoris's user 
 #   pass
    
    name
    nutriscore
    repere nutritionnel pour 100g
    lien page sur l'aliment openfoodfact
    image ou lien image
    id ou référence aliment recherché
    user foreikey
    """
