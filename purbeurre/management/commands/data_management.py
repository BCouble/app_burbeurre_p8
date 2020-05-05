from django.core.management import BaseCommand, CommandError
from django.db import IntegrityError

from purbeurre.libs.category import CreateCategory
from purbeurre.libs.constant import CATEGORYS0
from purbeurre.libs.food import CreateFood
from purbeurre.models import Category, FoodPurBeurre


class Command(BaseCommand):
    """ Import data in bdd purbeurre """
    help = 'Initializes categories and foods'

    def create_category_s0(self):
        """ init category s0 in db """
        for category in CATEGORYS0:
            try:
                Category.objects.create(name=category[0])
            except KeyError:
                pass
            except IntegrityError:
                pass

    def create_category_s1(self):
        """ init category s1 in db """
        cat = CreateCategory()
        cat_s1 = cat.create_s1_cat()
        for category in cat_s1:
            category_s = Category.objects.get(id=category[1])
            try:
                Category.objects.create(name=category[0], parent=category_s)
            except KeyError:
                pass
            except IntegrityError:
                pass

    def create_foods(self):
        """ search food in off """
        food = CreateFood()
        for category in CATEGORYS0:
            s_cat = Category.objects.get(id=category[1])
            for ss_cat in Category.objects.filter(parent=category[1]):
                search_term = (s_cat.name, ss_cat.name)
                result_search = food.search_food(search_term)
                food_for_insert = food.insert_data_in_dict(result_search)
                for row in food_for_insert:
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
                        else:
                            pass
                    except KeyError:
                        pass
                    except IntegrityError:
                        pass
                    except ValueError:
                        pass

    def handle(self, *args, **options):
        self.create_category_s0()
        self.create_category_s1()
        self.create_foods()

