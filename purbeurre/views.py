from django.views.generic import ListView
from django.views.generic.base import RedirectView, View, TemplateView
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


class DetailsFoodView(ListView):
    template_name = 'purbeurre/food_details.html'
    context_object_name = 'food_details'

    def get_queryset(self):
        """ Return subsittute with best nutriscore and best energy for 100gr """

        return FoodPurBeurre.objects.filter(id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nutriscore'] = ['a', 'b', 'c', 'd', 'e']
        return context


class FavorisFoodView(ListView):
    """ User's favoris """
    paginate_by = 6
    template_name = 'purbeurre/favoris.html'
    context_object_name = 'favoris'

    def get_context_data(self, *args, **kwargs):
        """ Add message """
        context = super().get_context_data(**kwargs)
        if self.kwargs:
            food = FoodPurBeurre.objects.get(id=self.kwargs['pk'])
            if Favoris.objects.filter(user=self.request.user, food=food).count() < 1:
                favoris = Favoris.objects.create(user=self.request.user, food=food)
                favoris.save()
                context['message'] = 'Vous venez de sauvegarder un aliment'
            else:
                context['message'] = 'Vous avez déjà sauvegardé l\'aliment'
            context['favoris'] = self.favoris
        return context

    def get_queryset(self):
        """ Return subsittute with best nutriscore and best energy for 100gr """
        self.favoris = Favoris.objects.filter(user=self.request.user)

        return self.favoris


class UserCreateView(FormView):
    template_name = 'purbeurre/signup.html'
    form_class = CustomUserCreationForm
    success_url = '/connect/'

    def form_valid(self, form):
        form.save()

        return super().form_valid(form)

    def form_invalid(self, form):

        return super().form_invalid(form)


class UserConnectView(FormView):
    """ Connect user """
    template_name = 'purbeurre/connect.html'
    form_class = CustomUserConnectForm
    success_url = '/'
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

    url = '/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)

        return super(UserLogoutView, self).get(request, *args, **kwargs)


class MlView(TemplateView):
    """ mentions légals"""

    template_name = 'mentionslegals.html'
