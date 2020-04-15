from django.urls import path

from . import views

app_name = 'purbeurre'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('h/', views.HomeView.as_view(), name='home'),
]