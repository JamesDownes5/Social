from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('event/<int:pk>/', views.EventView.as_view(), name='event'),
    path('create/', views.EventCreateView.as_view(), name='create'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('account/', views.account, name='account')
]