from django.test import TestCase, Client
from django.urls import reverse

from purbeurre.models import Category, FoodPurBeurre
from purbeurre.views import DetailsFoodView


class DetailsFoodPage(TestCase):

    def setUp(self):
        self.client = Client()
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

    def test_index_returns_200(self):
        """ Test statut code food details """
        response = self.client.get(reverse('purbeurre:food_details', args=(self.pk,)))
        self.assertEqual(response.status_code, 200)

    def test_view_with_resolver_match(self):
        """ Test view search food with request : nutella """
        response = self.client.get(reverse('purbeurre:food_details', args=(self.pk,)))
        self.assertEqual(response.resolver_match.func.__name__, DetailsFoodView.as_view().__name__)

    def test_query_set_food_details(self):
        """ Queryset test with products in result """
        response = self.client.get(reverse('purbeurre:food_details', args=(self.pk,)),
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertQuerysetEqual(list(response), (repr(r) for r in response))
