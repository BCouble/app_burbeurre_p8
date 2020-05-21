from django.views.generic import ListView
from django.views.generic.base import RedirectView, View
from django.views.generic.edit import FormView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, REDIRECT_FIELD_NAME, logout as auth_logout
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank

from .forms import SearchProductForm, CustomUserCreationForm, CustomUserConnectForm
from .models import CustomUser, FoodPurBeurre, Favoris


class IndexView(View):
    form_class = SearchProductForm
    initial = {'key': 'search_txt'}
    template_name = 'purbeurre/index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})


class SearchProductView(ListView):
    template_name = 'purbeurre/search_food.html'
    context_object_name = 'search_foods'
    slug_url_kwarg = 'search_text'

    def get_queryset(self):
        """ Return one product or 6 max """
        query = self.request.GET['search_text']
        search_vector = SearchVector('product_name_fr')
        search_query = SearchQuery(query)
        search_rank = SearchRank(search_vector, search_query)
        return FoodPurBeurre.objects.annotate(rank=search_rank).filter(rank__gte=0.05).order_by('-rank')[:6]


class SearchSubstituteView(ListView):
    template_name = 'purbeurre/search_substitute.html'
    context_object_name = 'search_substitute'

    def get_queryset(self):
        """ Return subsittute with best nutriscore and best energy for 100gr """
        category = FoodPurBeurre.objects.all().filter(id=self.kwargs['pk']).values()

        return FoodPurBeurre.objects.all().filter(category_s1=category[0]['category_s1_id']).order_by('nutriscore')[:6]


class SaveFoodView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'article-detail'

    def get_redirect_url(self, *args, **kwargs):
        print(self.kwargs)
        print(login)
        favoris = Favoris(user=self.__setattr__('_auth_user_id'), food=self.kwargs['pk'])

        return super(favoris.save()).get_redirect_url(*args, **kwargs)


class DetailsFoodView(ListView):
    template_name = 'purbeurre/food_details.html'
    context_object_name = 'food_details'

    def get_queryset(self):
        """ Return subsittute with best nutriscore and best energy for 100gr """

        return FoodPurBeurre.objects.filter(id=self.kwargs['pk'])


class FavorisFoodView(ListView):
    """ User's favoris """
    template_name = 'purbeurre/favoris.html'
    context_object_name = 'favoris'

    def get_queryset(self):
        """ Return subsittute with best nutriscore and best energy for 100gr """
        print(self.kwargs)

        return Favoris.objects.filter(id=self.kwargs['pk'])


class UserCreateView(FormView):
    template_name = 'purbeurre/signup.html'
    form_class = CustomUserCreationForm
    success_url = '/purbeurre/signup'

    def form_valid(self, form):
        form.save()

        return super().form_valid(form)

    def form_invalid(self, form):

        return super().form_invalid(form)


class UserConnectView(FormView):
    template_name = 'purbeurre/connect.html'
    form_class = CustomUserConnectForm
    success_url = '/purbeurre/'
    redirect_field_name = REDIRECT_FIELD_NAME

    def form_valid(self, form):
        login(self.request, form.get_user())

        return super(UserConnectView, self).form_valid(form)


class UserProfileView(LoginRequiredMixin, ListView):
    """ Display Profile User """
    template_name = 'purbeurre/profile.html'
    context_object_name = 'profile'

    def get_queryset(self):
        """ Return détails user's profile"""

        return CustomUser.objects.filter(id=self.kwargs['pk'])


class UserLogoutView(RedirectView):
    """ Deconnect Custom User """

    url = '/purbeurre/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)

        return super(UserLogoutView, self).get(request, *args, **kwargs)
