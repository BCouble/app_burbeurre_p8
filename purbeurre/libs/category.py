import requests

from purbeurre.config import CATEGORYS0
from purbeurre.libs.constant import BASE_URL_S_CAT, CATEGORY, NB_S_CAT


class CreateCategory:
    """ select, import data openfoodfact """
    def __init__(self):
        self.category = CATEGORYS0
        self.s1category = []

    def search_s1_category(self, obj):
        """ search s1 category for s0 category """
        response_s1_cat = requests.get(BASE_URL_S_CAT + obj + "/" + CATEGORY).json()

        return response_s1_cat

    def select_category_s0_and_search(self):
        """ retrieve sub-category """
        for row in self.category:
            sub_cat = self.search_s1_category(row[0])
            self.append_dict_sub_category(sub_cat, row[1])

        return self.s1category

    def append_dict_sub_category(self, sub_cat, id_s0):
        """ create dict sub-category """
        i = 1
        while i < NB_S_CAT:
            # limit the number of sub-categories according to the number of products
            if 200 < sub_cat['tags'][i]['products'] < 1000:
                self.s1category.append((sub_cat['tags'][i]['name'], id_s0))
            i += 1

        return self.s1category

