from django.contrib.auth import authenticate
from django.test import TestCase, Client
from django.urls import reverse

from purbeurre.models import Category, FoodPurBeurre, Favoris, CustomUser
from purbeurre.views import FavorisFoodView


class FavorisFoodPage(TestCase):
    def setUp(self):
        self.client = Client()
        CustomUser.objects.create_user(username='babatest', password='123AZEr!', email='baba.test@django.me')
        self.user = self.client.post(reverse('purbeurre:connect'),
                         {
                             'username': 'babatest',
                             'password': '123AZEr!'
                         })
        self.auth_user = authenticate(username='babatest', password='123AZEr!')
        Category.objects.create(name='ptit-dej')
        category_s0 = Category.objects.get(name='ptit-dej')
        Category.objects.create(name='nutella', parent=category_s0)
        cat_nutella = Category.objects.get(name='nutella')
        FoodPurBeurre.objects.create(
            product_name_fr='mini nutella',
            generic_name_fr='plus que mini nutella',
            nutriscore='c',
            nut_cent_gr=123,
            category_s1=cat_nutella,
            store='usa',
            link_off='http://nute.fr',
            link_img='http://nute.fr/mininut_img.jpeg',
        )
        query = FoodPurBeurre.objects.get(product_name_fr='mini nutella')
        self.pk = query.id
        Favoris.objects.create(user=self.auth_user, food=query)

    def test_return_favoris_of_user(self):
        """ Test save favoris and redirect View """
        query = Favoris.objects.get(user=self.auth_user)
        self.assertEqual(query.food.product_name_fr, 'mini nutella')
