from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('event', views.event, name='event'),
    path('create', views.create, name='create'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('account', views.account, name='account'),
]