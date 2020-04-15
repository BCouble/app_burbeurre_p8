from django.views import generic
from django.contrib.auth import authenticate, login
from .models import Message


class IndexView(generic.ListView):
    template_name = 'purbeurre/index.html'

    def homePage(self):
        """ home page """
        """ Welcome in purbeurre, et vive le gras ! """
        pass


class NavView(generic.ListView):
    template_name = 'purbeurre/nav.html'

    def coorporate(self):
        """ logo & name """
        pass

    def search(self):
        """ search header """
        pass

    def profil(self):
        """ user's profil """
        pass

    def carotte(self):
        """ user's favoris """
        pass

    def login(request):
        """ user's login """
        pass
        """
        error = False
    
        if request.method == "POST":
            form = ConnexionForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
                if user:  # Si l'objet renvoyé n'est pas None
                    login(request, user)  # nous connectons l'utilisateur
                else: # sinon une erreur sera affichée
                    error = True
        else:
            form = ConnexionForm()
    
        return render(request, 'connect.html', locals())
        """

    def logout(request):
        """ user de-connect """
        pass


class ContainerView():
    def searchsection(self):
        """ search's product """
        pass
        """ 
        01 phrase accroche
        02 le pourquoi de l'app
        03 form search
        """

    def presentationPurbeurre(self):
        """ Colette & Rémi """
        pass
        """
        01 Titre
        02 Story Stelling
        03 photo Col & rem 2 colonnes full one in smartphone
        """

    def purbeurreContact(self):
        """ contact's systems """
        pass
        """
        01 titre
        02 champs text ou phrase accroche ?
        03 Telephone et email 2 colonnes ou one in smartphone 
        """

    def headerProduct(self):
        """ product's header """
        pass
        """ 
        Construit les donné du header pour 3 :
        01 produit recherché
        02 produit sauvegardé
        03 profil user
        """

    def listProduct(self):
        """ product's list"""
        pass
        """
        Construit les datas pour afficher les substitu recherché ou les favoris
        """

    def dataProduct(self):
        """ product's datas """
        pass
        """
        nutriscore repère pour 100g
        lien openfoodfact
        """

    def compareProduct(self):
        """ product's compare """
        pass
        """ 
        01 : Affiche une liste pour sélectionner l'aliment recherché si plusieur choix possible
        02 : Si sur de l'aliment à substitué on affiche le résultat
        03 : Aucun retour message d'erreur : pas d'aliment pas de substitue ( pas de bras, pas de chocolat)
        """


class FooterView(generic.ListView):
    """ Footer project - Legal's mentions & Contact """
    def legalMention(self):
        """ legals mentions """
        pass

    def contact(self):
        """ contact purbeurre platform """
        pass
