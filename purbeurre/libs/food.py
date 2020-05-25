from purbeurre.libs.category import CreateCategory
import openfoodfacts
import json
import urllib
from urllib import parse, error, request

from purbeurre.libs.constant import FOOD, URL_LIST_FOOD


class CreateFood:
    def search_food(self, search_term):
        """ search in openfoodfact """

        payload = {
            'action': 'process',
            'json': '1',
            "search_terms": search_term,
            'tagtype_0': 'categories',
            'page_size': '200',
            'page': '1'
        }

        parameters = urllib.parse.urlencode(payload)
        url = URL_LIST_FOOD
        parameters = parameters.encode('utf-8')
        req = urllib.request.Request(url, parameters)

        try:
            response = urllib.request.urlopen(req)
            response_body = response.read().decode("utf-8")
            data = json.loads(response_body)

            return data
        except urllib.error.HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
            print(parameters)
            pass
        except urllib.error.URLError as e:
            print('We failed to reach a server.')
            print('Reason: ', e.reason)

    def insert_data_in_dict(self, data_food):
        """ load dict with search in off """
        list_food = []
        i = 0
        if int(data_food['count']) < 200:
            count = int(data_food['count'])
        else:
            count = 200
        while i < count:
            food = {"product_name_fr": "", "generic_name_fr": "", "id_s1_category": "", "store": "", "url": "",
                    "nutrition_grade_fr": "", "image_url": "", "energy_100g": ""}
            for key in food:
                try:
                    food[key] = data_food['products'][i][key]
                except KeyError:
                    pass
                if "energy_100g" in data_food['products'][i]["nutriments"]:
                    try:
                        food["energy_100g"] = data_food['products'][i]["nutriments"]["energy_100g"]
                    except KeyError:
                        pass
            list_food.append(food)
            i += 1

        return list_food
