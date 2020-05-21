from django.test import TestCase, Client

from purbeurre.models import Category, FoodPurBeurre
from purbeurre.config import CATEGORYS0


class SearchFoodPage(TestCase):

    def setUp(self):
        self.client = Client()
        Category.objects.create(name='search nutella')
        Category.objects.create(name='pizza')
        FoodPurBeurre.objects.create(
            product_name_fr='mini nutella',
            generic_name_fr='plus que mini nutella',
            nutriscore='e',
            nut_cent_gr=123,
            category_s1='search nutella',
            store='usa',
            link_off='http://nute.fr',
            link_img='http://nute.fr/mininut_img.jpeg',
        )
        FoodPurBeurre.objects.create(
            product_name_fr='big nutella',
            generic_name_fr='gros pot de nutella',
            nutriscore='e',
            nut_cent_gr=123,
            category_s1='search nutella',
            store='usa',
            link_off='http://nute.fr',
            link_img='http://nute.fr/bignut_img.jpeg',
        )
        FoodPurBeurre.objects.create(
            product_name_fr='pizza chorizo',
            generic_name_fr='La Pizz o Choz',
            nutriscore='a',
            nut_cent_gr=345,
            category_s1='pizza',
            store='Ikea',
            link_off='http://vivelebeurre.fr',
            link_img='http://vivelebeurre.fr/piz_choz.jpeg',
        )

    def test_import_category_niv_0(self):
        """ Test import category level 0 """