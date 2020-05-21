from unittest.mock import Mock

from django.test import TestCase

from purbeurre.config import FOODS_VIANDES_AND_STEACK
from purbeurre.libs.food import CreateFood


class ManageCategoryAPI(TestCase):
    """ Contains management for importing categories """
    def setUp(self):
        """ mock produced with meat and steak research """
        self.create_food = CreateFood()
        self.create_food.search_food = Mock(return_value=FOODS_VIANDES_AND_STEACK)
        search_term = ('viandes', 'steack')
        self.return_api_food = self.create_food.search_food(search_term)
        self.return_dict_food = self.create_food.insert_data_in_dict(self.return_api_food)

    def test_search_food(self):
        """ test page number """
        self.assertEqual(self.return_api_food['page'], '1')

    def test_count_food(self):
        """ test the number of products found """
        self.assertEqual(self.return_api_food['count'], 18)

    def test_page_size(self):
        """ test the page size configuration """
        self.assertEqual(self.return_api_food['page_size'], "200")

    def test_dat_first_line_product_name_fr(self):
        """ test data on the first product : product_name_fr """
        self.assertEqual(self.return_dict_food[0]['product_name_fr'], '4 steack hachés pur boeuf')

    def test_dat_first_line_generic_name_fr(self):
        """ test data on the first product : generic_name_fr """
        self.assertEqual(self.return_dict_food[0]['generic_name_fr'], '')

    def test_dat_first_line_stores(self):
        """ test data on the first product : stores """
        self.assertEqual(self.return_dict_food[0]['stores'], 'Leclerc')

    def test_dat_first_line_url(self):
        """ test data on the first product : url """
        self.assertEqual(self.return_dict_food[0]['url'], "https://fr.openfoodfacts.org/produit/3661112092085/4-steack-haches-pur-boeuf-ferial")

    def test_dat_first_line_nutrition_grade_fr(self):
        """ test data on the first product : nutrition_grade_fr """
        self.assertEqual(self.return_dict_food[0]['nutrition_grade_fr'], 'a')

    def test_dat_first_line_image_url(self):
        """ test data on the first product : image_url """
        self.assertEqual(self.return_dict_food[0]['image_url'], 'https://static.openfoodfacts.org/images/products/366/111/209/2085/front_fr.12.400.jpg')

    def test_dat_first_line_energy_100g(self):
        """ test data on the first product : energy_100g """
        self.assertEqual(self.return_dict_food[0]['energy_100g'], 523)

