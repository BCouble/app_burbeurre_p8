from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.template import loader
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.base import TemplateView, RedirectView, View
from django.views.generic.edit import CreateView, FormView
from django.shortcuts import render, redirect
from django.contrib.auth import login, REDIRECT_FIELD_NAME, logout as auth_logout

from .forms import SearchProductForm, CustomUserCreationForm, CustomUserConnectForm
from .models import CustomUser


class IndexView(TemplateView):
    template_name = 'purbeurre/index.html'


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


class UserLogoutView(RedirectView):
    """ Deconnect Custom User """

    url = '/purbeurre/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)

        return super(UserLogoutView, self).get(request, *args, **kwargs)


class SearchProductView(TemplateView):
    template_name = 'purbeurre/selectproduct.html'


"""
def productSearch(request):
    search_form = SearchProductForm()
    if search_form.is_valid():
        search = search_form.cleaned_data['search']
        envoi = True

    return render(request, 'purbeurre/tests.html', locals())



class IndexView(generic.ListView):
    template_name = 'purbeurre/index.html'

    def homePage(self):
        home page 
        Welcome in purbeurre, et vive le gras ! 
        pass
"""
