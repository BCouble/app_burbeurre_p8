from django.contrib.auth.views import LogoutView
from django.urls import path
from purbeurre.views import IndexView, UserCreateView, UserConnectView, UserLogoutView, SearchProductView, \
    SearchSubstituteView, DetailsFoodView, UserProfileView, FavorisFoodView
from . import views


app_name = 'purbeurre'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('signup/', UserCreateView.as_view(), name="signup"),
    path('connect/', UserConnectView.as_view(), name="connect"),
    path('user_logout/', UserLogoutView.as_view(), name="user_logout"),
    path('<int:pk>/profile', UserProfileView.as_view(), name="profile"),
    path('search_food/', SearchProductView.as_view(), name="search_food"),
    path('<int:pk>/search_substitute/', SearchSubstituteView.as_view(), name="search_substitute"),
    path('<int:pk>/food_details', DetailsFoodView.as_view(), name="food_details"),
    path('favoris/<int:pk>/', FavorisFoodView.as_view(), name="favoris"),
    path('favoris/', FavorisFoodView.as_view(), name="favoris"),
]
