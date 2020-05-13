from django.test import TestCase
from purbeurre.forms import SearchProductForm


class SearchProductFormTest(TestCase):
    """ Test champ of pai's search """
    def test_valid_data(self):
        """ Test if data is valid """
        form = SearchProductForm({
            'search': "nutella",
        })
        self.assertTrue(form.is_valid())

    def test_blank_data(self):
        """ Test if data is not valid """
        form = SearchProductForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'search_text': ['required'],
        })
