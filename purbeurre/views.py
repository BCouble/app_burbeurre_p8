from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.template import loader
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView, RedirectView, View
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, FormView, FormMixin
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, REDIRECT_FIELD_NAME, logout as auth_logout
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank
from .forms import SearchProductForm, CustomUserCreationForm, CustomUserConnectForm
from .models import CustomUser, FoodPurBeurre


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
        return FoodPurBeurre.objects.annotate(rank=search_rank).order_by('-rank')[:6]


class SearchSubstituteView(ListView):
    template_name = 'purbeurre/search_substitute.html'
    context_object_name = 'search_substitute'

    def get_queryset(self):
        """ Return subsittute with best nutriscore and best energy for 100gr """
        id_food = self.kwargs['pk']
        category = FoodPurBeurre.objects.all().filter(id=id_food).values()

        return FoodPurBeurre.objects.all().filter(category_s1=category[0]['category_s1_id']).order_by('nutriscore')[:6]


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


class UserProfileView(LoginRequiredMixin, DetailView):
    """ Display Profile User """
    model = CustomUser
    template_name = 'purbeurre/profile.html'


class UserLogoutView(RedirectView):
    """ Deconnect Custom User """

    url = '/purbeurre/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)

        return super(UserLogoutView, self).get(request, *args, **kwargs)
