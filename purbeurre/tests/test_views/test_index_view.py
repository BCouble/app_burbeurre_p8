from django.test import TestCase, Client
from django.urls import reverse

from purbeurre.views import IndexView


class IndexPageTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index_returns_200(self):
        """ Test statut code IndexView"""
        response = self.client.get(reverse('purbeurre:index'))
        self.assertEqual(response.status_code, 200)

    def test_indexview_as_view(self):
        """ Test resolved match with IndexView.as_view() """
        response = self.client.get(reverse('purbeurre:index'))
        self.assertEqual(response.resolver_match.func.__name__, IndexView.as_view().__name__)

    def test_view_uses_correct_template(self):
        """ Test template use """
        response = self.client.get(reverse('purbeurre:index'))
        self.assertTemplateUsed(response, 'purbeurre/index.html')

    def test_get_form_method(self):
        """ Test form method get """
        response = self.client.get(reverse('purbeurre:index'), {'search_text': 'nutella'})
        self.assertEqual(response.request['REQUEST_METHOD'], 'GET')

    def test_get_form_query_string(self):
        """ Test form query_string get """
        response = self.client.get(reverse('purbeurre:index'), {'search_text': 'nutella'})
        self.assertEqual(response.request['QUERY_STRING'], 'search_text=nutella')
