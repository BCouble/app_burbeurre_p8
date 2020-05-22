from django.test import TestCase, Client
from django.urls import reverse

from purbeurre.models import Category, FoodPurBeurre
from purbeurre.views import SearchSubstituteView


class SearchFoodPage(TestCase):

    def setUp(self):
        self.client = Client()
        Category.objects.create(name='ptit-dej')
        category_s0 = Category.objects.get(name='ptit-dej')
        Category.objects.create(name='nutella', parent=category_s0)
        cat_nutella = Category.objects.get(name='nutella')
        Category.objects.create(name='pizza', parent=category_s0)
        cat_pizza = Category.objects.get(name='pizza')
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
        FoodPurBeurre.objects.create(
            product_name_fr='big nutella',
            generic_name_fr='gros pot de nutella',
            nutriscore='e',
            nut_cent_gr=123,
            category_s1=cat_nutella,
            store='usa',
            link_off='http://nute.fr',
            link_img='http://nute.fr/bignut_img.jpeg',
        )
        FoodPurBeurre.objects.create(
            product_name_fr='pizza chorizo',
            generic_name_fr='La Pizz o Choz',
            nutriscore='a',
            nut_cent_gr=345,
            category_s1=cat_pizza,
            store='Ikea',
            link_off='http://vivelebeurre.fr',
            link_img='http://vivelebeurre.fr/bignut_img.jpeg',
        )
        FoodPurBeurre.objects.create(
            product_name_fr='choco mou',
            generic_name_fr='plus que mini nutella',
            nutriscore='b',
            nut_cent_gr=113,
            category_s1=cat_nutella,
            store='usa',
            link_off='http://nute.fr',
            link_img='http://nute.fr/mininut_img.jpeg',
        )
        FoodPurBeurre.objects.create(
            product_name_fr='moelle choc',
            generic_name_fr='',
            nutriscore='a',
            nut_cent_gr=90,
            category_s1=cat_nutella,
            store='usa',
            link_off='http://nute.fr',
            link_img='http://nute.fr/bignut_img.jpeg',
        )
        query = FoodPurBeurre.objects.get(product_name_fr='big nutella')
        self.pk = query.id
        query_pizza = FoodPurBeurre.objects.get(product_name_fr='pizza chorizo')
        self.pk2 = query_pizza.id

    def test_index_returns_200(self):
        """ Test statut code IndexView"""
        response = self.client.get(reverse('purbeurre:search_substitute', args=(self.pk,)))
        self.assertEqual(response.status_code, 200)

    def test_view_with_resolver_match(self):
        """ Test view search food with request : nutella """
        response = self.client.get(reverse('purbeurre:search_substitute', args=(self.pk,)))
        self.assertEqual(response.resolver_match.func.__name__, SearchSubstituteView.as_view().__name__)

    def test_search_zero_result(self):
        """ Queryset test with one response """
        response = self.client.get(reverse('purbeurre:search_substitute', args=(self.pk2,)))
        self.assertContains(response, "Nous n'avons pas trouvé de substitus !")
        self.assertQuerysetEqual(response.context['search_substitute'], ['<FoodPurBeurre: pizza chorizo>'])

    def test_search_text_one_key(self):
        """ Queryset test with 2 products in result """
        response = self.client.get(reverse('purbeurre:search_substitute', args=(self.pk,)), HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertQuerysetEqual(list(response), (repr(r) for r in response))





