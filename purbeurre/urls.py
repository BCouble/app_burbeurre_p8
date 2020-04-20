from django.urls import path

from . import views


#app_name = 'purbeurre'

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.productSearch, name="test"),
    path('signup/', views.signup, name="signup"),
]
