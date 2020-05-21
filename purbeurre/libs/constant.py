""" URL """
"""
----------------------------------------
Exemple url :

# Category
# https://fr.openfoodfacts.org/categories.json
# Sous category
# https://fr.openfoodfacts.org/categorie/sauces/categories.json
# Food 
# https://fr.openfoodfacts.org/cgi/search.pl?category=sauces&page_size=50&search_simple=1&action=process&page=2&json=1
----------------------------------------
"""

# Base
GEOLOC = "fr"
BASE_URL = "https://"+GEOLOC+".openfoodfacts.org/"

# Category
BASE_URL_S_CAT = BASE_URL+"categorie/"
CATEGORY = "categories.json"

# Food
CGI = "cgi/search.pl"
URL_LIST_FOOD = BASE_URL+CGI

""" CONFIG CATEGORIE """

NB_S_CAT = 150

""" CONFIG CATEGORIE """

LEN_CATEGORY = 20

""" DATA FOR PB OF OPENFOODFACT """
FOOD = {"product_name_fr": "", "generic_name_fr": "", "id_s1_category": "", "stores": "", "url": "", "nutrition_grade_fr": "", "image_url": "", "energy_100g": ""}

LABEL_PASSWORD1 = '<ul><li>Votre mot de passe ne doit pas être trop semblable à vos autres informations ' \
                  'personnelles.</li><li>Votre mot de passe doit contenir au moins 8 caractères.</li><li>Votre mot de ' \
                  'passe ne peut pas être un mot de passe couramment utilisé.</li><li>Votre mot de passe ne peut pas ' \
                  'être entièrement numérique.</li></ul> '
