from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('home/', views.index, name='index'),
    path('event/<int:pk>/', views.EventView.as_view(), name='event'),
    path('create/', views.EventCreateView.as_view(), name='create'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name="core/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="core/logout.html"), name='logout'),
    path('account/', views.account, name='account'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

