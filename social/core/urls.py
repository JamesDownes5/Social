from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('event/<int:pk>/', views.EventView.as_view(), name='event'),
    path('create/', views.EventCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', views.EventEditView.as_view(), name='edit'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name="core/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="core/logout.html"), name='logout'),
    path('account/', views.account, name='account'),
    path('send_friend_request/<int:userID>/', views.send_friend_request, name='send_friend_request'),
    path('accept_friend_request/<int:requestid>/', views.accept_friend_request, name='accept_friend_request'),
    path('decline_friend_request/<int:requestid>/', views.decline_friend_request, name='decline_friend_request'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

