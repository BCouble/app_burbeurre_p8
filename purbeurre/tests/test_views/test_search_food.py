from django.test import TestCase, Client, RequestFactory
from django.urls import reverse

from purbeurre.models import Category, FoodPurBeurre
from purbeurre.views import IndexView, SearchProductView


def create_category():
    """ Create search food of purbeurre database """
    return


def create_food():
    """ Create food for category """
    return


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

    def test_index_returns_200(self):
        """ Test statut code IndexView"""
        response = self.client.get(reverse('purbeurre:search_food'), {'search_text': 'nutella'})
        self.assertEqual(response.status_code, 200)

    def test_view_with_resolver_match(self):
        """ Test view search food with request : nutella """
        data = {'search_text': 'nutella'}
        response = self.client.get('/purbeurre/search_food/', data)
        self.assertEqual(response.resolver_match.func.__name__, SearchProductView.as_view().__name__)

    def test_get_redirect(self):
        """ Test redirect form search status code 302 """
        response = self.client.get(reverse('purbeurre:search_food'), {'search_text': 'nutella'})
        print(response)
        self.assertRedirects(response, 'purbeurre_search_food/')

    def test_search_text_empty(self):
        """ Queryset test with empty keyword """
        response = self.client.get(reverse('purbeurre:search_food'), {'search_text': ''})
        self.assertContains(response, "Nous n\'avons pas trouvé de produit correspondant à votre recherche !")
        self.assertQuerysetEqual(response.context['search_foods'], [])

    def test_search_text_one_key(self):
        """ Queryset test with empty keyword redirect index """
        response = self.client.get(reverse('purbeurre:search_food'), {'search_text': 'nutella'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        print(response.context['search_foods'])
        print(response.context)
        print(response.request)
        print(response.wsgi_request)
        self.assertQuerysetEqual(response.context['search_foods'], [])





