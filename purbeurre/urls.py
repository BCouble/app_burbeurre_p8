from django.contrib.auth.views import LogoutView
from django.urls import path
from purbeurre.views import IndexView, UserCreateView, UserConnectView, UserLogoutView
from . import views


app_name = 'purbeurre'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('signup/', UserCreateView.as_view(), name="signup"),
    path('connect/', UserConnectView.as_view(), name="connect"),
    path('user_logout/', UserLogoutView.as_view(), name="user_logout"),
]
