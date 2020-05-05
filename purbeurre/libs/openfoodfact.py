from purbeurre.libs.category import CreateCategory
from purbeurre.libs.constant import CATEGORYS0
from purbeurre.models import CategoryS0, CategoryS1, CategoryS2


class OpenFoodFact:
    """ Import data in bdd purbeurre """
    def __init__(self):
        """ init class category """
        category = CreateCategory()
        self.category_s1 = category.create_s1_cat()
        self.category_s2 = category.create_s2_cat()

    def import_cat_s0(self):
        """ import data category s0 """
        for category in CATEGORYS0:
            try:
                name_cat_s0 = CategoryS0.objects.get(name=category)
            except:
                name_cat_s0 = CategoryS0(name=category)
                name_cat_s0.save()

    def import_cat_s1(self):
        """ import data category s1 """
        for category in self.category_s1:
            try:
                name_cat_s1 = CategoryS1.objects.get(name=category)
            except:
                name_cat_s1 = CategoryS1(name=category)
                name_cat_s1.save()

    def import_cat_s2(self):
        """ import data category s0 """
        for category in self.category_s2:
            try:
                name_cat_s2 = CategoryS2.objects.get(name=category)
            except:
                name_cat_s2 = CategoryS2(name=category)
                name_cat_s2.save()
