import requests

from purbeurre.libs.constant import BASE_URL_S_CAT, CATEGORY, NB_S_CAT, LEN_CATEGORY, CATEGORYS0


class CreateCategory:
    """ select, import data openfoodfact """
    def __init__(self):
        self.category = CATEGORYS0
        self.all_category = []
        self.s1category = []

    def create_s1_cat(self):
        """select category s1"""
        s1category = []
        id = 1
        for row in self.category:
            obj = row[0]
            id_s0 = row[1]
            select_s1_cat = requests.get(BASE_URL_S_CAT + obj + "/" + CATEGORY).json()
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
