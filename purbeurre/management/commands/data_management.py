from django.core.management import BaseCommand
from django.db import IntegrityError

from purbeurre.config import CATEGORYS0
from purbeurre.libs.category import CreateCategory
from purbeurre.libs.food import CreateFood
from purbeurre.models import Category, FoodPurBeurre


class Command(BaseCommand):
    """ Import data in bdd purbeurre """
    help = 'Initializes categories and foods'

    def create_category_s0(self):
        """ Insert category s0 """
        for category in CATEGORYS0:
            try:
                Category.objects.create(name=category[0])
            except KeyError:
                pass
            except IntegrityError:
                pass

    def select_category_s0(self, id_s0):
        """ select instance category s0 """

        return Category.objects.get(id=id_s0)

    def create_category_s1(self):
        """ init category s1 in db """
        cat = CreateCategory()
        cat_s1 = cat.select_category_s0_and_search()
        for category in cat_s1:
            self.insert_category_S1(category[0], self.select_category_s0(category[1]))

    def insert_category_S1(self, name, parent):
        """ Insert category s1 with parent """
        try:
            Category.objects.create(name=name, parent=parent)
        except KeyError:
            pass
        except IntegrityError:
            pass

    def create_foods(self):
        """ search food in db purbeurre """
        food = CreateFood()
        for s_cat in Category.objects.filter(parent__isnull=True):
            for ss_cat in Category.objects.filter(parent=s_cat):
                result_search = food.search_food((s_cat.name, ss_cat.name))
                self.insert_food(food.insert_data_in_dict(result_search), ss_cat)

    def insert_food(self, food_list, ss_cat):
        """ insert food in db FoodPurBeurre """
        for row in food_list:
            try:
                if len(row['nutrition_grade_fr']) > 0:
                    FoodPurBeurre.objects.create(
                        product_name_fr=row['product_name_fr'],
                        generic_name_fr=row['generic_name_fr'],
                        nutriscore=row['nutrition_grade_fr'],
                        nut_cent_gr=row['energy_100g'],
                        category_s1=ss_cat,
                        store=row['store'],
                        link_off=row['url'],
                        link_img=row['image_url'],
                    )
            except KeyError as e:
                print("key error : " + e)
            except IntegrityError:
                print("integrity error : " + e)
            except ValueError:
                print("value error : " + e)

    def handle(self, *args, **options):
        self.create_category_s0()
        self.create_category_s1()
        self.create_foods()

