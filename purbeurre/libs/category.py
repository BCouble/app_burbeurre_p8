import requests

from purbeurre.config import CATEGORYS0
from purbeurre.libs.constant import BASE_URL_S_CAT, CATEGORY, NB_S_CAT


class CreateCategory:
    """ select, import data openfoodfact """
    def __init__(self):
        self.category = CATEGORYS0
        self.all_category = []
        self.s1category = []

    def search_s1_category(self, obj):
        """ search s1 category for s0 category """
        response_s1_cat = requests.get(BASE_URL_S_CAT + obj + "/" + CATEGORY).json()

        return response_s1_cat.json()

    def select_category_s0_and_search(self):
        """ retrieve sub-category """
        id_s0 = 1
        for row in self.category:
            sub_cat = self.search_s1_category(row[0])
            self.append_dict_sub_category(sub_cat, id_s0)
            id_s0 += 1

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

    def create_s1_cat(self):
        """ Select category s1 """
        s1category = []
        id = 1
        for row in self.category:
            obj = row[0]
            id_s0 = row[1]
            select_s1_cat = self.search_s1_category(obj)
            i = 0
            while i < NB_S_CAT:
                s1_cat = select_s1_cat['tags'][i]['name']
                nb_product = select_s1_cat['tags'][i]['products']
                # 20 to limit the number of subcategories
                if 200 < nb_product < 1000:
                    s1category.append((s1_cat, id_s0, id))
                    id += 1
                i += 1

        self.s1category = s1category
        return s1category

    def allCat(self):
        all_cat = []
        for row in self.category:
            s = row[1]
            for row1 in self.s1category:
                if row1[1] == s:
                    row_full = (row[0], row1[0])
                    all_cat.append(row_full)

        return all_cat


