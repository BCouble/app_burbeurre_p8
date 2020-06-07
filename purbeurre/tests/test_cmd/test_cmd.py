from unittest.mock import Mock

from django.test import TestCase

from purbeurre.libs.category import CreateCategory
from purbeurre.libs.food import CreateFood
from purbeurre.management.commands.data_management import Command
from purbeurre.models import Category, FoodPurBeurre
from purbeurre.config import CATEGORYS1_VIA, FOODS_VIANDES_AND_STEACK


class InsertDataWithCommand(TestCase):

    def setUp(self):
        self.command = Command()
        # category level 0
        self.only_s0 = self.command.create_category_s0()
        self.s0 = Category.objects.filter(id=1)
        self.s0p = Category.objects.filter(parent__isnull=True)

        self.create_category = CreateCategory()
        self.create_category.select_category_s0_and_search = Mock(return_value=CATEGORYS1_VIA)
        self.return_api_category = self.create_category.search_s1_category('viandes')
        self.return_dict_category = self.create_category.append_dict_sub_category(self.return_api_category, id_s0=1)

        self.create_food = CreateFood()
        self.create_food.search_food = Mock(return_value=FOODS_VIANDES_AND_STEACK)
        self.return_api_food = self.create_food.search_food(('viandes', 'steack'))
        self.return_dict_food = self.create_food.insert_data_in_dict(self.return_api_food)

    def test_import_category_niv_0(self):
        """ Test insert category level 0 """
        response = Category.objects.all()
        self.assertQuerysetEqual(list(response), (repr(r) for r in response))

    def test_import_category_niv_1(self):
        """ Test import category level 1 """
        for raw in self.return_dict_category:
            self.command.insert_category_S1(raw[0], self.s0p.first())
        response = Category.objects.get(name='Boudins')
        self.assertQuerysetEqual(response.name, ["'B'", "'o'", "'u'", "'d'", "'i'", "'n'", "'s'"])

    def test_import_food(self):
        """ Test import food """
        category_viande = Category.objects.get(name='viandes')
        Category.objects.create(name='steack', parent=category_viande)
        ss_cat = Category.objects.get(name='steack')
        self.command.insert_food(self.return_dict_food, ss_cat)
        response = FoodPurBeurre.objects.get(id=1)
        self.assertEqual(response.product_name_fr, 'Steacks hachés Pur Boeuf')





