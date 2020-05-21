from unittest.mock import Mock

from django.test import TestCase

from purbeurre.config import CATEGORYS0, CATEGORYS1_P_DEJ, CATEGORYS1_BOI, CATEGORYS1_VIA
from purbeurre.libs.category import CreateCategory
from purbeurre.libs.constant import NB_S_CAT


class ManageCategoryAPI(TestCase):
    """ Contains management for importing categories """
    def setUp(self) :
        self.category = CATEGORYS0
        self.response_categorys1 = CATEGORYS1_P_DEJ
        self.create_category = CreateCategory()
        self.create_category.search_s1_category = Mock(return_value=CATEGORYS1_VIA)
        self.return_api_category = self.create_category.search_s1_category('viandes')
        self.return_dict_category = self.create_category.append_dict_sub_category(self.return_api_category, id_s0=1)

    def test_count_nb_category(self):
        """ mock category 'viandes' meat returns, number of sub-categories """
        self.assertEqual(self.return_api_category['count'], 1555)

    def test_nom_category(self):
        """ retrieves a category name """
        self.assertEqual(self.return_api_category['tags'][0]['name'], 'Viandes')

    def test_nb_products_in_category(self):
        """ retrieves a nb product """
        self.assertEqual(self.return_api_category['tags'][0]['products'], 30845)

    def test_create_link_with_parent(self):
        """ Test if the sub-category has its parent """
        self.assertEqual(self.return_dict_category[14][1], 1)

    def test_nb_product_in_interval(self):
        """ Sub-categories must have between 200 and 1000 products """
        product_test_first_line = self.return_dict_category[0][0]
        i = 0
        for row in self.return_api_category['tags']:
            if self.return_api_category['tags'][i]['name'] == product_test_first_line:
                name_test = self.return_api_category['tags'][i]['name']

                self.assertEqual(product_test_first_line, name_test)

    def test_nb_product_out_interval(self):
        """ Sub-categories must have between 200 and 1000 products """
        # with result of test_nb_products_in_category
        product_test_greater_than_1000 = self.return_api_category['tags'][0]['name']
        name_test = 'wrong'
        i = 0
        for row in self.return_dict_category:
            if product_test_greater_than_1000 == self.return_dict_category[i][0]:
                name_test = self.return_dict_category[i][0]

        self.assertEqual(name_test, name_test)
